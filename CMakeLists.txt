cmake_minimum_required(VERSION 3.1) # CMake_最低版本_需求

project("Hello World") # 建立一個CMake專案，並給予專案名稱

add_executable(hello-world) # 建立一個CMake目標，目標為可執行檔

target_sources(hello-world PRIVATE "main.cpp") # 指定建置該CMake目標時所使用的來源檔案