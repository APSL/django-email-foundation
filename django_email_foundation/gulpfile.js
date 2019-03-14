var gulp = require('gulp');
var yargs = require('yargs');
var panini = require('panini');
var inky = require('inky');
var open = require('gulp-open');

// Constants
var TEMPLATES_SOURCE = yargs.argv.templates_source;
var TEMPLATES_TARGET = yargs.argv.templates_target;
var IGNORE_FILES = yargs.argv.ignore_files;
var PREVIEW_URL = yargs.argv.preview_url;

// Initial checks
if (!TEMPLATES_SOURCE) {
  console.log('The templates dir parameter is required.');
  process.exit(1);
}

if (!TEMPLATES_TARGET) {
  console.log('The destination dir is required.');
  process.exit(1);
}

// Tasks definition
gulp.task('watch',
  gulp.series(build, preview, watch));

// Methods
function build() {

  var sources = [TEMPLATES_SOURCE + '/pages/**/*.html'];
  if (IGNORE_FILES !== '') {
    var files = IGNORE_FILES.split(',');
    var filesToMove = [];
    for (var i = 0; i < files.length; i++) {
      sources.push('!' + TEMPLATES_SOURCE + '/pages/**/' + files[i]);
      filesToMove.push(TEMPLATES_SOURCE + '/pages/**/' + files[i]);
    }

    // And now is important to move this files to the destination folder
    gulp.src(filesToMove)
      .pipe(gulp.dest(TEMPLATES_TARGET));
  }

  return gulp.src(sources)
    .pipe(panini({
      root: TEMPLATES_SOURCE + '/pages/',
      layouts: TEMPLATES_SOURCE + '/layouts/',
      partials: TEMPLATES_SOURCE + '/partials/',
      helpers: TEMPLATES_SOURCE + '/helpers/',
    }))
    .pipe(inky())
    .pipe(gulp.dest(TEMPLATES_TARGET));
}

function watch() {
  gulp.watch(TEMPLATES_SOURCE + '/pages/**/*.html').on('all', gulp.series(build));
}

function preview(done) {
  gulp.src(__filename)
    .pipe(open({ uri: PREVIEW_URL }));
  done();
}
