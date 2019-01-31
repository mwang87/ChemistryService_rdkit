build:
	docker build -t chemicalwebservice2 .

clear:
	docker rm chemicalwebservice2 || :

background: clear
	docker run -d -p 5066:5000 --name chemicalwebservice2 chemicalwebservice2 /app/run_server.sh

interactive: clear
	docker run -it -p 5066:5000 --name chemicalwebservice2 chemicalwebservice2 /app/run_server.sh

shell: clear
	docker run -it -p 5066:5000 --name chemicalwebservice2 chemicalwebservice2 bash
