{
  "targets": [
    {
      'target_name': 'libninja',
      'type': 'static_library',
      'include_dirs': [
        'ninja/src',
      ],
      'sources': [
        'ninja/src/build.cc',
        'ninja/src/build_log.cc',
        'ninja/src/clean.cc',
        'ninja/src/debug_flags.cc',
        'ninja/src/depfile_parser.cc',
        'ninja/src/deps_log.cc',
        'ninja/src/disk_interface.cc',
        'ninja/src/edit_distance.cc',
        'ninja/src/eval_env.cc',
        'ninja/src/graph.cc',
        'ninja/src/graphviz.cc',
        'ninja/src/lexer.cc',
        'ninja/src/line_printer.cc',
        'ninja/src/manifest_parser.cc',
        'ninja/src/metrics.cc',
        'ninja/src/state.cc',
        'ninja/src/util.cc',
        'ninja/src/version.cc',
      ],
      'conditions': [
        ['OS == "win"', {
          'msvs_configuration_attributes': {
            'CharacterSet': '0',
          },
          'defines': [
            'NINJA_PYTHON="python.exe"',
            'NOMINMAX',
            '_CRT_SECURE_NO_WARNINGS',
            '_VARIADIC_MAX=10',
          ],
          'sources': [
            'ninja/src/getopt.c',
            'ninja/src/includes_normalize-win32.cc',
            'ninja/src/minidump-win32.cc',
            'ninja/src/msvc_helper-win32.cc',
            'ninja/src/msvc_helper_main-win32.cc',
            'ninja/src/subprocess-win32.cc',
          ],
        }, { # else: OS != "win", currently is linux only.
          'defines': [
            'NINJA_PYTHON="python"',
            'USE_PPOLL',
            'NINJA_HAVE_BROWSE',
          ],
          'sources': [
            'ninja/src/browse.cc',
            'ninja/src/subprocess-posix.cc',
          ],
        }]
      ],
    },
  ],
}
