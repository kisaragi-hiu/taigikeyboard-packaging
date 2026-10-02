.ONESHELL:

build:
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
