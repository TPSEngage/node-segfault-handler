{
  "targets": [
    {
      "target_name": "segfault-handler",
      "sources": [
        "src/segfault-handler.cpp"
      ],
      "cflags": [ "-O0", "-funwind-tables" ],
      "xcode_settings": {
        "MACOSX_DEPLOYMENT_TARGET": "10.9",
        "OTHER_CFLAGS": [ "-O0", "-funwind-tables" ],
        "CLANG_CXX_LIBRARY": "libc++"
      },
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
