# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `greet()` takes a new `punctuation` argument: `greet("Hee", ".")` returns `Hello, Hee.` (before: always `!`).

### Fixed

- `greet()` with an empty or blank name returns `Hello, world!` (before: `Hello, !`).

## [0.1.0] - 2026-11-09

### Added

- `greet()` function and command-line greeting (`python greet.py <name>`, default `world`).
