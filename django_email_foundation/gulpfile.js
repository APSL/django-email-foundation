var gulp = require('gulp');
var yargs = require('yargs');
var panini = require('panini');
var inky = require('inky');
var open = require('gulp-open');
var debug = require('gulp-debug');
var plugins = require('gulp-load-plugins');
var fs = require('fs');
var siphon = require('siphon-media-query');
var lazypipe = require('lazypipe');
var os = require('os');

var $ = plugins();

// Constants
var TEMPLATES_SOURCE = yargs.argv.templates_source;
var TEMPLATES_TARGET = yargs.argv.templates_target;
var STATIC_TARGET = yargs.argv.static_target;
var IGNORE_FILES = yargs.argv.ignore_files;
var PREVIEW_URL = yargs.argv.preview_url;

console.log('Sources:', TEMPLATES_SOURCE);
console.log('Target:', TEMPLATES_TARGET);
console.log('Static:', STATIC_TARGET);
console.log('Ignore files:', IGNORE_FILES);
console.log('Preview Url:', PREVIEW_URL);

// Initial checks
if (!TEMPLATES_SOURCE) {
  console.log('The templates source path is required.');
  process.exit(1);
}

if (!TEMPLATES_TARGET) {
  console.log('The templates target path is required.');
  process.exit(1);
}

if (!STATIC_TARGET) {
  console.log('The static target path is required.')
  process.exit(1);
}

// Tasks definition
gulp.task('watch',
  gulp.series(build, sass, images, inline, preview, watch));

// Methods
function build() {
  panini.refresh();

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
    .pipe(debug())
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
  gulp.watch(TEMPLATES_SOURCE).on('all', gulp.series(build, sass, images, inline));
}

function preview(done) {
  gulp.src(__filename)
    .pipe(open({ uri: PREVIEW_URL }));
  done();
}

function sass() {
  return gulp.src(TEMPLATES_SOURCE + '/assets/scss/app.scss')
    .pipe(debug())
    .pipe($.sass({
      includePaths: ['node_modules/foundation-emails/scss']
    }).on('error', $.sass.logError))
    .pipe($.uncss({
      html: [TEMPLATES_TARGET + '/**/*.html']
    }))
    .pipe(gulp.dest(os.tmpdir() + '/django-email-foundation/'));
}

function images() {
  return gulp.src(TEMPLATES_SOURCE + '/assets/img/**/*')
    .pipe($.imagemin())
    .pipe(gulp.dest(STATIC_TARGET + '/img'));
}

function inline() {
  return gulp.src(TEMPLATES_TARGET + '/**/*.html')
    .pipe(inliner(os.tmpdir() + '/django-email-foundation/app.css'))
    .pipe(gulp.dest(TEMPLATES_TARGET))
}

function inliner(css) {
  var css = fs.readFileSync(css).toString();
  var mqCss = siphon(css);

  var pipe = lazypipe()
    .pipe($.inlineCss, {
      applyStyleTags: false,
      removeStyleTags: true,
      preserveMediaQueries: true,
      removeLinkTags: false,
      extraCss: css
    })
    .pipe($.htmlmin, {
      collapseWhitespace: true,
      minifyCSS: true
    });

  return pipe();
}
