cmake_minimum_required(VERSION 3.13)

project(11)
set(CMAKE_CXX_STANDARD 20)


set(CMAKE_CXX_FLAGS_RELEASE "-O2 -Wall")
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall")

add_executable(11 main.cpp)
