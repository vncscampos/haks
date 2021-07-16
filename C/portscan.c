#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main (int argc, char* argv[]) {
	int mysocket;
	int connection;

	int port;
	int init = 0;
	int final = 65535;

	struct sockaddr_in target;

	for(port=init; port<final; port++){

		mysocket = socket(AF_INET, SOCK_STREAM, 0);
		target.sin_family = AF_INET;
		target.sin_port = htons(port);
		target.sin_addr.s_addr = inet_addr(argv[1]);

		connection = connect(mysocket, (struct sockaddr *)&target, sizeof(target));

		if(connection == 0) {
			printf("Porta: %d aberta \n", port);
			close(mysocket);
			close(connection);
		} else {
			close(mysocket);
			close(connection);
		}
	}
	return 0;
}
