# -*- mode: org; -*-

In lieu of a better place to put these... I named this .ex just in case other names get picked up by Debian tooling.

** Building

Ugly way to include Cargo dependencies in the source package.

#+begin_src sh
(cd linux && cargo vendor)
mv linux/vendor debian
# for whatever reason certain vendored packages have .gitignore files in them
# which debuild understandably omits, but then checksum checks fail.
find debian/vendor -path "*/.cargo-checksum.json" \
    -exec sed -i s/'"[a-z0-9\/-]*\/\.gitignore":"[a-z0-9]\+",'//g '{}' ';'
find debian/vendor -path "*/.cargo-checksum.json" \
    -exec sed -i s/'"[a-z0-9\/-]*\/[a-z0-9]*\.a":"[a-z0-9]\+",'//g '{}' ';'
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
