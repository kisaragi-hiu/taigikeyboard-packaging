.ONESHELL:

# Just using this file as a marker
src/README.md:
	@cd src
	echo "Asking uscan which version we are unpacking..."
	VERSION=$$(uscan --report-status --dehs 2>/dev/null | grep '<upstream-version>' | sed s/'<\/\?upstream-version>//g')
	echo "The version is $$VERSION."
	FILE=../taigikeyboard-"$$VERSION".tar.gz
	if [ ! -f "$$FILE" ]; then
		echo "Downloading the tarball..."
		uscan -dd
	fi
	echo "Unpacking the tarball..."
	tar -xf "$$FILE" --strip-components=1

.PHONY: build
build: src/README.md
	cd src
	(cd linux && cargo vendor)
	mv linux/vendor debian
	# for whatever reason certain vendored packages have .gitignore files in them
	# which debuild understandably omits, but then checksum checks fail.
	find debian/vendor -path "*/.cargo-checksum.json" \
		-exec sed -i s/'"[a-z0-9\/-]*\/\.gitignore":"[a-z0-9]\+",'//g '{}' ';'
	find debian/vendor -path "*/.cargo-checksum.json" \
		-exec sed -i s/'"[a-z0-9\/-]*\/[a-z0-9]*\.a":"[a-z0-9]\+",'//g '{}' ';'
	debuild -S -sa
