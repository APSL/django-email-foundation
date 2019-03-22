import os
import pytest

from django_email_foundation.utils import get_relative_from_manage_path


@pytest.mark.parametrize(
    'getcwd,path,expected',
    [
        ('/home/demo/workspace/my_project/src', 'src/module/emails', 'module/emails'),
        ('/home/demo/workspace/my_project', 'module/emails', 'module/emails'),
        ('/home/demo/workspace/my_project/src', 'src/emails/sources', 'emails/sources'),
        ('/home/demo/workspace/my_project', 'test/emails/sources', 'test/emails/sources'),
    ]
)
def test_get_relative_from_manage_path(getcwd, path, expected, monkeypatch):
    def getcwd_patched():
        return getcwd
    monkeypatch.setattr(os, 'getcwd', getcwd_patched)
    assert get_relative_from_manage_path(path) == expected
