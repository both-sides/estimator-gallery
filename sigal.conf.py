# All configuration values have a default; values that are commented out serve
# to show the default. Default values are specified when modified in this
# example config file

# Gallery title. Can be set here or as the '--title' option of the `sigal
# build` command, or in the 'index.md' file of the source directory.
# The priority order is: cli option > settings file > index.md file
# title = "Sigal test gallery"

# ---------------------
# General configuration
# ---------------------

# Source directory. Can be set here or as the first argument of the `sigal
# build` command
source = "pictures"

# Destination directory. Can be set here or as the second argument of the
# `sigal build` command (default: '_build')
# destination = '_build'

# Theme :
# - colorbox (default), galleria, photoswipe, or the path to a custom theme
# directory
theme = "galleria"

# Theme for galleria (https://galleriajs.github.io/themes/)
# galleria_theme = 'classic'

# Author. Used in the footer of the pages and in the author meta tag.
# author = ''

# Use originals in gallery (default: False). If True, this will bypass all
# processing steps (resize, auto-orient, recompress, and any plugin-specific
# step).
# Originals will be symlinked if orig_link = True, else they will be copied.
# use_orig = False

# Path to a CSS file that can be used to customize themes
# user_css =

# Enable autoplay (galleria only)
# autoplay = False

# ----------------
# Image processing (ignored if use_orig = True)
# ----------------

# Size of resized image (default: (640, 480))
img_size = (800, 600)

# Max input image size in pixels (default: None, i.e. use PIL default)
# This option sets `PIL.Image.MAX_IMAGE_PIXELS` in case you want to
# convert/resize very large images.
# max_img_pixels = None

# Output format of images (default: None, i.e. use input format)
# img_format = "JPEG"

# Show a map of the images where possible?
# This option only has an effect on the galleria theme for the while.
# The leaflet_provider setting allow to customize the tile provider (see
# https://github.com/leaflet-extras/leaflet-providers#providers)
# show_map = False
# leaflet_provider = 'OpenStreetMap.Mapnik'
# map_height = '500px'

# File extensions that should be treated as images
# img_extensions = [".jpg", ".jpeg", ".png", ".gif", ".heic", ".tif", ".tiff", ".webp"]

# Pilkit processor used to resize the image
# (see http://pilkit.readthedocs.org/en/latest/#processors)
# - ResizeToFit: fit the image within the specified dimensions (default)
# - ResizeToFill: crop THE IMAGE it to the exact specified width and height
# - SmartResize: identical to ResizeToFill, but uses entropy to crop the image
# - None: don't resize
# img_processor = 'ResizeToFit'

# Autorotate images
# Warning: this setting is not compatible with `copy_exif_data` (see below),
# because Sigal can't save the modified Orientation tag (currently Pillow can't
# write EXIF).
# autorotate_images = True

# If True, EXIF data from the original image is copied to the resized image
# copy_exif_data = False

# Python's datetime format string used for the EXIF date formatting
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# datetime_format = '%c'

# Display generated datetime in the resulting output
# display_timestamp = False

# Jpeg options
# jpg_options = {'quality': 85,
#                'optimize': True,
#                'progressive': True}

# --------------------
# Thumbnail generation
# --------------------

# Generate thumbnails
# make_thumbs = True

# Subdirectory of the thumbnails
# thumb_dir = 'thumbnails'

# Prefix and/or suffix for thumbnail filenames (default: '')
# thumb_prefix = ''
# thumb_suffix = '.tn'

# Thumbnail size (default: (200, 150))
# For the galleria theme, use 280 px for the width
# For the colorbox and photoswipe theme, use 200 px for the width
thumb_size = (280, 210)

# Crop the image to fill the box
# thumb_fit = True

# When using thumb_fit, specifies what we should crop
# for usage see
# http://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
# thumb_fit_centering = (0.5, 0.5)

# Delay in seconds to avoid black thumbnails in videos with fade-in
# thumb_video_delay = 0
# Max retries to generate a non-black thumbnail
# thumb_video_black_retries = 0
# For each retry, advance another N seconds on top of original delay
# thumb_video_black_retry_offset = 1
# A thumbnail with more than max_colors will not be considered "all black"
# thumb_video_black_max_colors = 4

# Keep original image (default: False)
# keep_orig = False

# Subdirectory for original images
# orig_dir = 'original'

# Use symbolic links instead of copying the original images
# orig_link = False

# Use symbolic links that are relative to the source directory instead of
# absolute paths
# rel_link = False

# Attribute of Album objects which is used to sort medias (eg 'title'). To
# sort on a metadata key, use 'meta.key'.
# albums_sort_attr = 'name'

# Reverse sort for albums
# albums_sort_reverse = False

# Attribute of Media objects which is used to sort medias. 'date' can be used
# to sort with EXIF dates, and 'meta.key' to sort on a metadata key (which then
# must exist for all images).
# medias_sort_attr = 'filename'

# Reverse sort for medias
# medias_sort_reverse = False

# Filter directories and files.
# The settings take a list of patterns matched with the fnmatch module on the
# path relative to the source directory:
# http://docs.python.org/3/library/fnmatch.html
ignore_directories = []
ignore_files = []

# -------------
# Video options
# -------------

# Video converter binary (can be 'avconv' on certain GNU/Linux distributions)
# video_converter = 'ffmpeg'

# File extensions that should be treated as video files
# video_extensions = ['.mov', '.avi', '.mp4', '.webm', '.ogv', '.3gp']

# Video format
# specify an alternative format, valid are 'webm' (default) and 'mp4'
# video_format = 'webm'

# Webm options
# Options used in ffmpeg to encode the webm video. You may want to read
# http://ffmpeg.org/trac/ffmpeg/wiki/vpxEncodingGuide
# Be aware of the fact these options need to be passed as strings. If you are
# using avconv (for example with Ubuntu), you will need to adapt the settings.
# webm_options = ['-crf', '10', '-b:v', '1.6M',
#                 '-qmin', '4', '-qmax', '63']

# Webm options for 2-pass encoding
# Options used to encode the webm video on the second pass.
# Set to None by default, set to an array if a second pass is desired.
# webm_options_second_pass = None


# MP4 options
# Options used to encode the mp4 video. You may want to read
# https://trac.ffmpeg.org/wiki/Encode/H.264
# mp4_options = ['-crf', '23' ]

# MP4 options for 2-pass encoding
# Options used to encode the mp4 video on the second pass.
# Set to None by default, set to an array if a second pass is desired.
# mp4_options_second_pass = None


# Size of resized video (default: (480, 360))
# Set this to None if no resizing is desired on the video.
# video_size = (480, 360)

# If the desired video extension and filename are the same, the video will
# not be converted. If a transcode to different quality is required,
# set this to True to force convert it. False by default.
# video_always_convert = False

# -------------
# Miscellaneous
# -------------

# Write HTML files. If False, sigal will only process the images.
# write_html = True

# Name of the generated HTML files
# output_filename = 'index.html'

# Add output filename (see above) to the URLs
# index_in_url = False

# A list of links (tuples (title, URL))
# links = [('Example link', 'http://example.org'),
#          ('Another link', 'http://example.org')]

# Google Analytics tracking code (UA-xxxx-x)
# google_analytics = ''

# Google Tag Manager tracking code (GTM-xxxxxx)
# google_tag_manager = ''

# Piwik tracking
# tracker_url must not contain trailing slash.
# Example : {'tracker_url': 'http://stats.domain.com', 'site_id' : 2}
# piwik = {'tracker_url': '', 'site_id' : 0}

# Specify a different locale. If set to '', the default locale is used.
# locale = ''

# Define language used on main <html> tag in templates
# html_language = 'en'

# List of files to copy from the source directory to the destination.
# A symbolic link is used if ``orig_link`` is set to True (see above).
# files_to_copy = (('extra/robots.txt', 'robots.txt'),
#                  ('extra/favicon.ico', 'favicon.ico'),)

# Colorbox theme config
# The column size is given in number of column of the css grid of the Skeleton
# framework which is used for this theme: http://www.getskeleton.com/#grid
# Then the image size must be adapted to fit the column size.
# The default is 3 columns (176px).
# colorbox_column_size = 3

# Site Logo - Use a logo file in the sidebar
# Only for colorbox currently, it could be adapted for other themes
# You must place the logo file into the theme's static images folder, which
# can be done using 'files_to_copy':
# files_to_copy = (('extra/logo.png', 'static/logo.png'))
# site_logo = 'logo.png'

# --------
# Plugins
# --------

# List of plugins to use. The values must be a path than can be imported.
# Another option is to import the plugin and put the module in the list, but
# this will break with the multiprocessing feature (the settings dict obtained
# from this file must be serializable).
# plugins = [
#     'sigal.plugins.adjust',
#     'sigal.plugins.compress_assets',
#     'sigal.plugins.copyright',
#     'sigal.plugins.encrypt',
#     'sigal.plugins.extended_caching',
#     'sigal.plugins.feeds',
#     'sigal.plugins.media_page',
#     'sigal.plugins.nomedia',
#     'sigal.plugins.nonmedia_files',
#     'sigal.plugins.watermark',
#     'sigal.plugins.zip_gallery',
# ]

# Adjust the image after resizing it. A default value of 1.0 leaves the images
# untouched.
# adjust_options = {'color': 1.0,
#                   'brightness': 1.0,
#                   'contrast': 1.0,
#                   'sharpness': 1.0}

# Settings for compressing static assets
# compress_assets_options = {
#    'method': 'gzip' # Or 'zopfli' or 'brotli'
# }

# Add a copyright text on the image (default: '')
# copyright = "© An example copyright message"

# Settings for encryption plugin
# encrypt_options = {
#    'password': 'password',
#    'ask_password': False
# }

# Settings for nonmedia_files plugin.
# nonmedia_files_options = {
#     'ext_as_thumb': True,
#     'ignore_ext': ['.md'],
#     'thumb_bg_color': (255, 255, 255),
#     'thumb_font': None, # name/path of font file
#     'thumb_font_color': (0, 0, 0),
#     'thumb_font_size': 40, # only applies when a font is selected
# }

# Set zip_gallery to either False or a file name. The file name can
# be formatted python style with an 'album' variable, for example
# '{album.name}.zip'. The final archive will contain all resized or
# original files (depending on `zip_media_format`).
# zip_gallery = False   # False or 'archive.zip'
# zip_media_format = 'resized'  # 'resized' or 'orig'
# zip_skip_if_exists = False # Skip archive generation if archive is
# already present. Warning: new photos in an album won't be added to archive

orig_link = True # keep and link full‑res 
img_size = None # don’t resize the “big” image
thumbnail_size = (350,350) # only thumbnails shrink


