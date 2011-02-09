# Copyright (c) 2009 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'variables': {
    'chromium_code': 1,
  },
  'targets': [
    {
      'target_name': 'cefclient',
      'type': 'executable',
      'mac_bundle': 1,
      'msvs_guid': '6617FED9-C5D4-4907-BF55-A90062A6683F',
      'dependencies': [
        '../third_party/npapi/npapi.gyp:npapi',
        'libcef',
        'libcef_dll_wrapper',
      ],
      'defines': [
        'USING_CEF_SHARED',
      ],
      'include_dirs': [
        '.',
        '..',
      ],
      'sources': [
        'include/cef.h',
        'include/cef_nplugin.h',
        'include/cef_runnable.h',
        'include/cef_tuple.h',
        'include/cef_wrapper.h',
        'tests/cefclient/binding_test.cpp',
        'tests/cefclient/binding_test.h',
        'tests/cefclient/cefclient.cpp',
        'tests/cefclient/cefclient.h',
        'tests/cefclient/download_handler.cpp',
        'tests/cefclient/download_handler.h',
        'tests/cefclient/extension_test.cpp',
        'tests/cefclient/extension_test.h',
        'tests/cefclient/resource_util.h',
        'tests/cefclient/scheme_test.cpp',
        'tests/cefclient/scheme_test.h',
        'tests/cefclient/string_util.cpp',
        'tests/cefclient/string_util.h',
        'tests/cefclient/util.h',
      ],
      'mac_bundle_resources': [
        'tests/cefclient/mac/cefclient.icns',
        'tests/cefclient/mac/data/',
        'tests/cefclient/mac/English.lproj/InfoPlist.strings',
        'tests/cefclient/mac/English.lproj/MainMenu.xib',
        'tests/cefclient/mac/Info.plist',
      ],
      'mac_bundle_resources!': [
        # TODO(mark): Come up with a fancier way to do this (mac_info_plist?)
        # that automatically sets the correct INFOPLIST_FILE setting and adds
        # the file to a source group.
        'tests/cefclient/mac/Info.plist',
      ],
      'xcode_settings': {
        'INFOPLIST_FILE': 'tests/cefclient/mac/Info.plist',
      },
      'conditions': [
        ['OS=="win"', {
          'msvs_settings': {
            'VCLinkerTool': {
              # Set /SUBSYSTEM:WINDOWS.
              'SubSystem': '2',
              'EntryPointSymbol' : 'wWinMainCRTStartup',
            },
          },
          'link_settings': {
            'libraries': [
              '-lcomctl32.lib',
              '-lshlwapi.lib',
              '-lrpcrt4.lib',
              '-lopengl32.lib',
              '-lglu32.lib',
            ],
          },
          'sources': [
            'tests/cefclient/cefclient.ico',
            'tests/cefclient/cefclient.rc',
            'tests/cefclient/cefclient_win.cpp',
            'tests/cefclient/clientplugin.cpp',
            'tests/cefclient/clientplugin.h',
            'tests/cefclient/plugin_test.cpp',
            'tests/cefclient/plugin_test.h',
            'tests/cefclient/Resource.h',
            'tests/cefclient/res/cefclient.ico',
            'tests/cefclient/res/logo.jpg',
            'tests/cefclient/res/logoball.jpg',
            'tests/cefclient/res/small.ico',
            'tests/cefclient/res/uiplugin.html',
            'tests/cefclient/resource_util_win.cpp',
            'tests/cefclient/uiplugin.cpp',
            'tests/cefclient/uiplugin.h',
            'tests/cefclient/uiplugin_test.cpp',
            'tests/cefclient/uiplugin_test.h',
          ],
        }],
        [ 'OS=="mac"', {
          'product_name': 'cefclient',
          'variables': {
            'repack_path': '../tools/data_pack/repack.py',
          },
          'actions': [
            {
              # TODO(mark): Make this work with more languages than the
              # hardcoded en-US.
              'action_name': 'repack_locale',
              'variables': {
                'pak_inputs': [
                  '<(SHARED_INTERMEDIATE_DIR)/webkit/webkit_chromium_resources.pak',
                  '<(SHARED_INTERMEDIATE_DIR)/webkit/webkit_strings_en-US.pak',
                  '<(SHARED_INTERMEDIATE_DIR)/webkit/webkit_resources.pak',
                ],
              },
              'inputs': [
                '<(repack_path)',
                '<@(pak_inputs)',
              ],
              'outputs': [
                '<(INTERMEDIATE_DIR)/repack/cefclient.pak',
              ],
              'action': ['python', '<(repack_path)', '<@(_outputs)', '<@(pak_inputs)'],
              'process_outputs_as_mac_bundle_resources': 1,
            },
          ],
          'copies': [
            {
              # Add library dependencies and app launcher script to the bundle.
              'destination': '<(PRODUCT_DIR)/cefclient.app/Contents/MacOS/',
              'files': [
                '<(PRODUCT_DIR)/libcef.dylib',
                '<(PRODUCT_DIR)/libffmpegsumo.dylib',
                'tests/cefclient/cefclient_mac_app.sh',
              ],
            },
            {
              # Add the WebCore resources to the bundle.
              'destination': '<(PRODUCT_DIR)/cefclient.app/Contents/',
              'files': [
                '../third_party/WebKit/Source/WebCore/Resources/',
              ],
            },
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
            ],
          },
          'sources': [
            'tests/cefclient/cefclient_mac.mm',
          ],
        }],
        [ 'OS=="linux" or OS=="freebsd" or OS=="openbsd"', {
          'sources': [
            'tests/cefclient/cefclient_gtk.cpp',
          ],
        }],
      ],
    },
    {
      'target_name': 'cef_unittests',
      'type': 'executable',
      'msvs_guid': '8500027C-B11A-11DE-A16E-B80256D89593',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:base_i18n',
        '../base/base.gyp:test_support_base',
        '../testing/gtest.gyp:gtest',
        '../third_party/icu/icu.gyp:icui18n',
        '../third_party/icu/icu.gyp:icuuc',
        'libcef',
        'libcef_dll_wrapper',
      ],
      'sources': [
        'tests/unittests/request_unittest.cc',
        'tests/unittests/run_all_unittests.cc',
        'tests/unittests/stream_unittest.cc',
        'tests/unittests/string_unittest.cc',
        'tests/unittests/test_handler.h',
        'tests/unittests/test_suite.h',
        'tests/unittests/url_unittest.cc',
        'tests/unittests/v8_unittest.cc',
        'tests/unittests/web_urlrequest_unittest.cc',
        'tests/unittests/xml_reader_unittest.cc',
        'tests/unittests/zip_reader_unittest.cc',
      ],
      'include_dirs': [
        '.',
        '..',
      ],
    },
    {
      'target_name': 'patcher',
      'type': 'none',
      'msvs_guid': 'A6D0953E-899E-4C60-AB6B-CAE75A44B8E6',
      'conditions': [
        ['OS=="win"', {
          'actions': [{
            'action_name': 'patch_source',
            'msvs_cygwin_shell': 0,
            'inputs': [
              'tools/patch_source.bat',
            ],
            'outputs': [
              'tools/patch_source.bat.output',
            ],
            'action': ['', '<@(_inputs)'],
          }],
        }, { # OS!="win"
          'actions': [{
            'action_name': 'patch_source',
            'inputs': [
              'tools/patch_source.sh',
            ],
            'outputs': [
              'tools/patch_source.sh.output',
            ],
            'action': ['<@(_inputs)'],
          }],
        }],
      ],
    },
    {
      'target_name': 'libcef',
      'type': 'shared_library',
      'msvs_guid': 'C13650D5-CF1A-4259-BE45-B1EBA6280E47',
      'dependencies': [
        '../app/app.gyp:app_base',
        '../base/base.gyp:base',
        '../base/base.gyp:base_i18n',
        '../build/temp_gyp/googleurl.gyp:googleurl',
        '../gfx/gfx.gyp:gfx',
        '../media/media.gyp:media',
        '../net/net.gyp:net',
        '../net/net.gyp:net_resources',
        '../printing/printing.gyp:printing',
        '../sdch/sdch.gyp:sdch',
        '../skia/skia.gyp:skia',
        '../third_party/bzip2/bzip2.gyp:bzip2',
        '../third_party/ffmpeg/ffmpeg.gyp:ffmpeg',
        '../third_party/icu/icu.gyp:icui18n',
        '../third_party/icu/icu.gyp:icuuc',
        '../third_party/libjpeg/libjpeg.gyp:libjpeg',
        '../third_party/libpng/libpng.gyp:libpng',
        '../third_party/libxml/libxml.gyp:libxml',
        '../third_party/libxslt/libxslt.gyp:libxslt',
        '../third_party/modp_b64/modp_b64.gyp:modp_b64',
        '../third_party/WebKit/Source/WebCore/WebCore.gyp/WebCore.gyp:webcore',
        '../third_party/WebKit/WebKit/chromium/WebKit.gyp:concatenated_devtools_css',
        '../third_party/WebKit/WebKit/chromium/WebKit.gyp:concatenated_devtools_js',
        '../third_party/WebKit/WebKit/chromium/WebKit.gyp:devtools_html',
        '../third_party/WebKit/WebKit/chromium/WebKit.gyp:inspector_resources',
        '../third_party/WebKit/WebKit/chromium/WebKit.gyp:webkit',
        '../third_party/zlib/zlib.gyp:zlib',
        '../ui/ui.gyp:ui_base',
        '../webkit/support/webkit_support.gyp:appcache',
        '../webkit/support/webkit_support.gyp:blob',
        '../webkit/support/webkit_support.gyp:database',
        '../webkit/support/webkit_support.gyp:fileapi',
        '../webkit/support/webkit_support.gyp:glue',
        '../webkit/support/webkit_support.gyp:webkit_gpu',
        '../webkit/support/webkit_support.gyp:webkit_resources',
        '../webkit/support/webkit_support.gyp:webkit_strings',
        'libcef_static',
      ],
      'defines': [
        'BUILDING_CEF_SHARED',
      ],
      'include_dirs': [
        '.',
        '..',
      ],
      # Avoid "RC1102: internal error : too many arguments to RCPP" error by
      # explicitly specifying a short list of resource include directories.
      'resource_include_dirs' :  [
        '.',
        '..',
      ],
      'sources': [
        'include/cef.h',
        'include/cef_capi.h',
        'include/cef_export.h',
        'include/cef_nplugin.h',
        'include/cef_nplugin_capi.h',
        'include/cef_ptr.h',
        'include/cef_string.h',
        'include/cef_string_list.h',
        'include/cef_string_map.h',
        'include/cef_string_types.h',
        'include/cef_string_wrappers.h',
        'include/cef_types.h',
        'libcef_dll/cef_logging.h',
        'libcef_dll/cpptoc/browser_cpptoc.cc',
        'libcef_dll/cpptoc/browser_cpptoc.h',
        'libcef_dll/cpptoc/cpptoc.h',
        'libcef_dll/cpptoc/frame_cpptoc.cc',
        'libcef_dll/cpptoc/frame_cpptoc.h',
        'libcef_dll/cpptoc/post_data_cpptoc.cc',
        'libcef_dll/cpptoc/post_data_cpptoc.h',
        'libcef_dll/cpptoc/post_data_element_cpptoc.cc',
        'libcef_dll/cpptoc/post_data_element_cpptoc.h',
        'libcef_dll/cpptoc/request_cpptoc.cc',
        'libcef_dll/cpptoc/request_cpptoc.h',
        'libcef_dll/cpptoc/response_cpptoc.cc',
        'libcef_dll/cpptoc/response_cpptoc.h',
        'libcef_dll/cpptoc/stream_reader_cpptoc.cc',
        'libcef_dll/cpptoc/stream_reader_cpptoc.h',
        'libcef_dll/cpptoc/stream_writer_cpptoc.cc',
        'libcef_dll/cpptoc/stream_writer_cpptoc.h',
        'libcef_dll/cpptoc/v8value_cpptoc.cc',
        'libcef_dll/cpptoc/v8value_cpptoc.h',
        'libcef_dll/cpptoc/web_urlrequest_cpptoc.cc',
        'libcef_dll/cpptoc/web_urlrequest_cpptoc.h',
        'libcef_dll/cpptoc/xml_reader_cpptoc.cc',
        'libcef_dll/cpptoc/xml_reader_cpptoc.h',
        'libcef_dll/cpptoc/zip_reader_cpptoc.cc',
        'libcef_dll/cpptoc/zip_reader_cpptoc.h',
        'libcef_dll/ctocpp/ctocpp.h',
        'libcef_dll/ctocpp/download_handler_ctocpp.cc',
        'libcef_dll/ctocpp/download_handler_ctocpp.h',
        'libcef_dll/ctocpp/handler_ctocpp.cc',
        'libcef_dll/ctocpp/handler_ctocpp.h',
        'libcef_dll/ctocpp/read_handler_ctocpp.cc',
        'libcef_dll/ctocpp/read_handler_ctocpp.h',
        'libcef_dll/ctocpp/scheme_handler_ctocpp.cc',
        'libcef_dll/ctocpp/scheme_handler_ctocpp.h',
        'libcef_dll/ctocpp/scheme_handler_factory_ctocpp.cc',
        'libcef_dll/ctocpp/scheme_handler_factory_ctocpp.h',
        'libcef_dll/ctocpp/task_ctocpp.cc',
        'libcef_dll/ctocpp/task_ctocpp.h',
        'libcef_dll/ctocpp/v8handler_ctocpp.cc',
        'libcef_dll/ctocpp/v8handler_ctocpp.h',
        'libcef_dll/ctocpp/web_urlrequest_client_ctocpp.cc',
        'libcef_dll/ctocpp/web_urlrequest_client_ctocpp.h',
        'libcef_dll/ctocpp/write_handler_ctocpp.cc',
        'libcef_dll/ctocpp/write_handler_ctocpp.h',
        'libcef_dll/libcef_dll.cc',
        'libcef_dll/resource.h',
        'libcef_dll/transfer_util.cpp',
        'libcef_dll/transfer_util.h',
      ],
      'conditions': [
        ['OS=="win"', {
          'dependencies': [
            '../breakpad/breakpad.gyp:breakpad_handler',
          ],
          'sources': [
            '$(OutDir)/obj/global_intermediate/webkit/webkit_chromium_resources.rc',
            '$(OutDir)/obj/global_intermediate/webkit/webkit_resources.rc',
            '$(OutDir)/obj/global_intermediate/webkit/webkit_strings_en-US.rc',
            'include/cef_types_win.h',
            'include/cef_win.h',
            'libcef_dll/libcef_dll.rc',
          ],
          'link_settings': {
            'libraries': [
              '-lcomctl32.lib',
            ],
          },
        }]
      ],
    },
    {
      'target_name': 'libcef_dll_wrapper',
      'type': 'static_library',
      'msvs_guid': 'A9D6DC71-C0DC-4549-AEA0-3B15B44E86A9',
      'dependencies': [
        '../third_party/npapi/npapi.gyp:npapi',
        'libcef',
      ],
      'defines': [
        'USING_CEF_SHARED',
      ],
      'include_dirs': [
        '.',
        '..',
      ],
      'sources': [
        'include/cef_wrapper.h',
        'libcef_dll/cef_logging.h',
        'libcef_dll/cpptoc/cpptoc.h',
        'libcef_dll/cpptoc/download_handler_cpptoc.cc',
        'libcef_dll/cpptoc/download_handler_cpptoc.h',
        'libcef_dll/cpptoc/handler_cpptoc.cc',
        'libcef_dll/cpptoc/handler_cpptoc.h',
        'libcef_dll/cpptoc/read_handler_cpptoc.cc',
        'libcef_dll/cpptoc/read_handler_cpptoc.h',
        'libcef_dll/cpptoc/scheme_handler_cpptoc.cc',
        'libcef_dll/cpptoc/scheme_handler_cpptoc.h',
        'libcef_dll/cpptoc/scheme_handler_factory_cpptoc.cc',
        'libcef_dll/cpptoc/scheme_handler_factory_cpptoc.h',
        'libcef_dll/cpptoc/task_cpptoc.cc',
        'libcef_dll/cpptoc/task_cpptoc.h',
        'libcef_dll/cpptoc/v8handler_cpptoc.cc',
        'libcef_dll/cpptoc/v8handler_cpptoc.h',
        'libcef_dll/cpptoc/web_urlrequest_client_cpptoc.cc',
        'libcef_dll/cpptoc/web_urlrequest_client_cpptoc.h',
        'libcef_dll/cpptoc/write_handler_cpptoc.cc',
        'libcef_dll/cpptoc/write_handler_cpptoc.h',
        'libcef_dll/ctocpp/browser_ctocpp.cc',
        'libcef_dll/ctocpp/browser_ctocpp.h',
        'libcef_dll/ctocpp/ctocpp.h',
        'libcef_dll/ctocpp/frame_ctocpp.cc',
        'libcef_dll/ctocpp/frame_ctocpp.h',
        'libcef_dll/ctocpp/post_data_ctocpp.cc',
        'libcef_dll/ctocpp/post_data_ctocpp.h',
        'libcef_dll/ctocpp/post_data_element_ctocpp.cc',
        'libcef_dll/ctocpp/post_data_element_ctocpp.h',
        'libcef_dll/ctocpp/request_ctocpp.cc',
        'libcef_dll/ctocpp/request_ctocpp.h',
        'libcef_dll/ctocpp/response_ctocpp.cc',
        'libcef_dll/ctocpp/response_ctocpp.h',
        'libcef_dll/ctocpp/stream_reader_ctocpp.cc',
        'libcef_dll/ctocpp/stream_reader_ctocpp.h',
        'libcef_dll/ctocpp/stream_writer_ctocpp.cc',
        'libcef_dll/ctocpp/stream_writer_ctocpp.h',
        'libcef_dll/ctocpp/v8value_ctocpp.cc',
        'libcef_dll/ctocpp/v8value_ctocpp.h',
        'libcef_dll/ctocpp/web_urlrequest_ctocpp.cc',
        'libcef_dll/ctocpp/web_urlrequest_ctocpp.h',
        'libcef_dll/ctocpp/xml_reader_ctocpp.cc',
        'libcef_dll/ctocpp/xml_reader_ctocpp.h',
        'libcef_dll/ctocpp/zip_reader_ctocpp.cc',
        'libcef_dll/ctocpp/zip_reader_ctocpp.h',
        'libcef_dll/transfer_util.cpp',
        'libcef_dll/transfer_util.h',
        'libcef_dll/wrapper/cef_byte_read_handler.cc',
        'libcef_dll/wrapper/cef_xml_object.cc',
        'libcef_dll/wrapper/cef_zip_archive.cc',
        'libcef_dll/wrapper/libcef_dll_wrapper.cc',
      ],
    },
    {
      'target_name': 'libcef_static',
      'type': 'static_library',
      'msvs_guid': 'FA39524D-3067-4141-888D-28A86C66F2B9',
      'defines': [
        'BUILDING_CEF_SHARED',
      ],
      'include_dirs': [
        '.',
        '..',
        '../third_party/WebKit/WebKit/chromium/public'
      ],
      'dependencies': [
        '../app/app.gyp:app_base',
        '../base/base.gyp:base',
        '../base/base.gyp:base_i18n',
        '../build/temp_gyp/googleurl.gyp:googleurl',
        '../gfx/gfx.gyp:gfx',
        '../media/media.gyp:media',
        '../net/net.gyp:net',
        '../net/net.gyp:net_resources',
        '../printing/printing.gyp:printing',
        '../sdch/sdch.gyp:sdch',
        '../skia/skia.gyp:skia',
        '../third_party/bzip2/bzip2.gyp:bzip2',
        '../third_party/ffmpeg/ffmpeg.gyp:ffmpeg',
        '../third_party/icu/icu.gyp:icui18n',
        '../third_party/icu/icu.gyp:icuuc',
        '../third_party/libjpeg/libjpeg.gyp:libjpeg',
        '../third_party/libpng/libpng.gyp:libpng',
        '../third_party/libxml/libxml.gyp:libxml',
        '../third_party/libxslt/libxslt.gyp:libxslt',
        '../third_party/modp_b64/modp_b64.gyp:modp_b64',
        '../third_party/WebKit/Source/WebCore/WebCore.gyp/WebCore.gyp:webcore',
        '../third_party/WebKit/WebKit/chromium/WebKit.gyp:webkit',
        '../third_party/zlib/zlib.gyp:zlib',
        '../ui/ui.gyp:ui_base',
        '../webkit/support/webkit_support.gyp:appcache',
        '../webkit/support/webkit_support.gyp:blob',
        '../webkit/support/webkit_support.gyp:database',
        '../webkit/support/webkit_support.gyp:fileapi',
        '../webkit/support/webkit_support.gyp:glue',
        '../webkit/support/webkit_support.gyp:webkit_gpu',
        '../webkit/support/webkit_support.gyp:webkit_resources',
        '../webkit/support/webkit_support.gyp:webkit_strings',
      ],
      'sources': [
        'include/cef.h',
        'include/cef_export.h',
        'include/cef_nplugin.h',
        'include/cef_ptr.h',
        'include/cef_string.h',
        'include/cef_string_list.h',
        'include/cef_string_map.h',
        'include/cef_string_types.h',
        'include/cef_string_wrappers.h',
        'include/cef_types.h',
        'libcef/browser_appcache_system.cc',
        'libcef/browser_appcache_system.h',
        'libcef/browser_database_system.cc',
        'libcef/browser_database_system.h',
        'libcef/browser_devtools_agent.cc',
        'libcef/browser_devtools_agent.h',
        'libcef/browser_devtools_callargs.cc',
        'libcef/browser_devtools_callargs.h',
        'libcef/browser_devtools_client.cc',
        'libcef/browser_devtools_client.h',
        'libcef/browser_file_system.cc',
        'libcef/browser_file_system.h',
        'libcef/browser_file_writer.cc',
        'libcef/browser_file_writer.h',
        'libcef/browser_impl.cc',
        'libcef/browser_impl.h',
        'libcef/browser_navigation_controller.cc',
        'libcef/browser_navigation_controller.h',
        'libcef/browser_request_context.cc',
        'libcef/browser_request_context.h',
        'libcef/browser_resource_loader_bridge.cc',
        'libcef/browser_resource_loader_bridge.h',
        'libcef/browser_settings.cc',
        'libcef/browser_settings.h',
        'libcef/browser_socket_stream_bridge.cc',
        'libcef/browser_socket_stream_bridge.h',
        'libcef/browser_web_worker.h',
        'libcef/browser_webcookiejar_impl.cc',
        'libcef/browser_webcookiejar_impl.h',
        'libcef/browser_webblobregistry_impl.cc',
        'libcef/browser_webblobregistry_impl.h',
        'libcef/browser_webstoragearea_impl.cc',
        'libcef/browser_webstoragearea_impl.h',
        'libcef/browser_webstoragenamespace_impl.cc',
        'libcef/browser_webstoragenamespace_impl.h',
        'libcef/browser_webkit_glue.cc',
        'libcef/browser_webkit_glue.h',
        'libcef/browser_webkit_init.h',
        'libcef/browser_webview_delegate.cc',
        'libcef/browser_webview_delegate.h',
        'libcef/browser_zoom_map.cc',
        'libcef/browser_zoom_map.h',
        'libcef/cef_context.cc',
        'libcef/cef_context.h',
        'libcef/cef_process.cc',
        'libcef/cef_process.h',
        'libcef/cef_process_io_thread.cc',
        'libcef/cef_process_io_thread.h',
        'libcef/cef_process_sub_thread.cc',
        'libcef/cef_process_sub_thread.h',
        'libcef/cef_process_ui_thread.cc',
        'libcef/cef_process_ui_thread.h',
        'libcef/cef_string_list.cc',
        'libcef/cef_string_map.cc',
        'libcef/cef_string_types.cc',
        'libcef/cef_thread.cc',
        'libcef/cef_thread.h',
        'libcef/dom_storage_area.cc',
        'libcef/dom_storage_area.h',
        'libcef/dom_storage_common.h',
        'libcef/dom_storage_context.cc',
        'libcef/dom_storage_context.h',
        'libcef/dom_storage_namespace.cc',
        'libcef/dom_storage_namespace.h',
        'libcef/external_protocol_handler.h',
        'libcef/http_header_utils.cc',
        'libcef/http_header_utils.h',
        'libcef/request_impl.cc',
        'libcef/request_impl.h',
        'libcef/response_impl.cc',
        'libcef/response_impl.h',
        'libcef/scheme_impl.cc',
        'libcef/simple_clipboard_impl.cc',
        'libcef/stream_impl.cc',
        'libcef/stream_impl.h',
        'libcef/tracker.h',
        'libcef/v8_impl.cc',
        'libcef/v8_impl.h',
        'libcef/web_urlrequest_impl.cc',
        'libcef/web_urlrequest_impl.h',
        'libcef/webview_host.h',
        'libcef/webwidget_host.h',
        'libcef/xml_reader_impl.cc',
        'libcef/xml_reader_impl.h',
        'libcef/zip_reader_impl.cc',
        'libcef/zip_reader_impl.h',
      ],
      'conditions': [
        ['OS=="win"', {
          'dependencies': [
            '../breakpad/breakpad.gyp:breakpad_handler',
          ],
          'sources': [
            'include/cef_types_win.h',
            'include/cef_win.h',
            'libcef/browser_drag_delegate.cc',
            'libcef/browser_drag_delegate.h',
            'libcef/browser_drop_delegate.cc',
            'libcef/browser_drop_delegate.h',
            'libcef/browser_impl_win.cc',
            'libcef/browser_webkit_glue_win.cc',
            'libcef/browser_webview_delegate_win.cc',
            'libcef/cef_process_ui_thread_win.cc',
            'libcef/external_protocol_handler_win.cc',
            'libcef/printing/print_settings.cc',
            'libcef/printing/print_settings.h',
            'libcef/printing/win_printing_context.cc',
            'libcef/printing/win_printing_context.h',
            'libcef/webview_host_win.cc',
            'libcef/webwidget_host_win.cc',
          ],
        }],
        [ 'OS=="mac"', {
          'sources': [
            'include/cef_types_mac.h',
            'include/cef_mac.h',
            'libcef/browser_impl_mac.mm',
            'libcef/browser_webkit_glue_mac.mm',
            'libcef/browser_webview_delegate_mac.mm',
            'libcef/browser_webview_mac.h',
            'libcef/browser_webview_mac.mm',
            'libcef/cef_process_ui_thread_mac.mm',
            'libcef/external_protocol_handler_mac.mm',
            'libcef/webview_host_mac.mm',
            'libcef/webwidget_host_mac.mm',
          ],
        }],
        [ 'OS=="linux" or OS=="freebsd" or OS=="openbsd"', {
          'sources': [
            'include/cef_types_linux.h',
            'include/cef_linux.h',
            'libcef/browser_impl_gtk.cc',
            'libcef/browser_webkit_glue_gtk.cc',
            'libcef/browser_webview_delegate_gtk.cc',
            'libcef/cef_process_ui_thread_gtk.cc',
            'libcef/external_protocol_handler_gtk.cc',
            'libcef/webview_host_gtk.cc',
            'libcef/webwidget_host_gtk.cc',
          ],
        }],
      ],
    },
  ]
}
