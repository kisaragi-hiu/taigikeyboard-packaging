# -*- mode: org; -*-

In lieu of a better place to put these... I named this .ex just in case other names get picked up by Debian tooling.

** Building

Ugly way to include Cargo dependencies in the source package.

#+begin_src sh
(cd linux && cargo vendor)
mv linux/vendor debian
# passed to dpkg-buildpackage.
# -S: --build=source, build just a source package
# -sa: source always includes orig
debuild -S -sa
#+end_src

** Cloning

This probably works?

#+begin_src sh
git clone https://github.com/kisaragi-hiu/taigikeyboard-debian.git
git checkout debian/latest
git remote add upstreamvcs https://github.com/taigikeyboard/taigikeyboard.git
#+end_src

** Importing new upstream version

#+begin_src sh
git fetch upstreamvcs
gbp import-orig --uscan
#+end_src
