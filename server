#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>

main()
{
        struct sockaddr_in client, server;
        int i=0,s, n, sock, g, j, left, right, flag;
        char b1[20], b2[10], b3[10], b4[10];
        s = socket(AF_INET, SOCK_STREAM, 0);
        server.sin_family = AF_INET;
        server.sin_port = 2000;
        server.sin_addr.s_addr = inet_addr("127.0.0.1");
        bind(s, (struct sockaddr*)&server, sizeof server);
        listen(s, 1);
        n = sizeof client;

        sock = accept(s, (struct sockaddr*)&client, &n);
        for(;;){
                recv(sock, &b1, sizeof(b1), 0);
                printf("\nThe string received is:%s\n", b1);
                if (strlen(b1) == 0)
                        flag = 1;
                else {
                 for (i = 0; b1[i]!='\0'; i++){
         if(b1[i] >= 'a' && b1[i] <= 'z') {
         b1[i] = b1[i] - 32;}
      }
   }
                send(sock, &b1, sizeof(b1), 0);
                break;
        }
        close(sock);

                close(s);
}
