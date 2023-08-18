build:
	docker build -t living_dex .

help:
	docker run -it --rm --name living_dex -v ${PWD}:/usr/src/app -w /usr/src/app living_dex python -m living_dex -h

run:
	docker run -it --rm --name living_dex -v ${PWD}:/usr/src/app -w /usr/src/app living_dex python -m living_dex --input=data/dex.json --output=data/output.txt