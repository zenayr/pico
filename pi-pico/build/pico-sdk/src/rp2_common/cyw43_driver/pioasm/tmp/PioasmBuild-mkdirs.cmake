# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "E:/Projects/VSARM/sdk/pico/pico-sdk/tools/pioasm"
  "E:/Projects/pico/pi-pico/build/pioasm"
  "E:/Projects/pico/pi-pico/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm"
  "E:/Projects/pico/pi-pico/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/tmp"
  "E:/Projects/pico/pi-pico/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src/PioasmBuild-stamp"
  "E:/Projects/pico/pi-pico/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src"
  "E:/Projects/pico/pi-pico/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src/PioasmBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "E:/Projects/pico/pi-pico/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src/PioasmBuild-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "E:/Projects/pico/pi-pico/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src/PioasmBuild-stamp${cfgdir}") # cfgdir has leading slash
endif()
