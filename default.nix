{ pkgs ? import <nixpkgs> {} }:
pkgs.pkgsCross.mingw32.callPackage ./derivation.nix {}
