.ONESHELL:

.PHONY: src
src: src/README.md

# Just using this file as a marker
src/README.md:
	@cd src
	echo "Asking uscan which version we are unpacking..."
	VERSION=$$(uscan --report-status --dehs 2>/dev/null | grep '<upstream-version>' | sed s/'<\/\?upstream-version>//g')
	echo "The version is $$VERSION."
	FILE=../taigikeyboard_"$$VERSION".orig.tar.xz
	if [ ! -f "$$FILE" ]; then
		echo "Downloading the tarball..."
		uscan -dd
	fi
	echo "Unpacking the tarball..."
	tar -xf "$$FILE" --strip-components=1

local-build: src
	cd src
	debuild -b

# Ugly way to include Cargo dependencies in the source package.
.PHONY: build
build: src
	cd src
	# prepare to include vendored files in the debian archive, which will be
	# unpacked & configured during override_dh_auto_build
	(cd linux && cargo vendor)
	mv linux/vendor debian
	# for whatever reason certain vendored packages have .gitignore files in them
	# which debuild understandably omits, but then checksum checks fail.
	find debian/vendor -path "*/.cargo-checksum.json" \
		-exec sed -i s/'"[a-z0-9\/-]*\/\.gitignore":"[a-z0-9]\+",'//g '{}' ';'
	find debian/vendor -path "*/.cargo-checksum.json" \
		-exec sed -i s/'"[a-z0-9\/-]*\/[a-z0-9]*\.a":"[a-z0-9]\+",'//g '{}' ';'
	# work around vendored binary files
	find debian/vendor '(' \
		-path "*.ttf" \
		-or -path "*.png" \
		-or -path "*.wasm" \
		-or -path "*.lib" \
		-or -path "*.dll" \
		-or -path "*.font" \
		-or -path "*.ttc" \
		-or -path "*.otb" \
		')' -delete
	# and (try to) delete them from checksum files
	find debian/vendor -path "*/.cargo-checksum.json" \
		-exec sed -i s/'"[a-z0-9\/-]*\/[a-z0-9.@]\.(ttf|png|wasm|lib|dll|font|ttc|otb)":"[a-z0-9]\+",'//g '{}' ';'
	# add back final newline if they are stripped
	# https://unix.stackexchange.com/a/31955
	find debian/vendor -path "*/.cargo-checksum.json" \
		-exec sed -i -e '$$a\\' '{}' ';'
	# then finally build the .dsc package
	debuild -S -sa

clean:
	# We only clean within src/! This avoids deleting the original tarballs.
	cd src
	git clean -xdf
