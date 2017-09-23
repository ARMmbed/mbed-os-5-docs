## Cellular TCP sockets

This example opens a TCP socket with an echo server and undergoes a TCP transaction. Connection logic is the same as in the previous example.

```cpp
#include "mbed.h"
#include "UDPSocket.h"
#include "OnboardCellularInterface.h"

// SIM pin code goes here
#define PIN_CODE    "1234"

// Network credentials like APN go here, e.g.,
// "apn, username, password"
#define CREDENTIALS "internet"

// Number of retries /
#define RETRY_COUNT 3

// Cellular network interface object
OnboardCellularInterface iface;

// Echo server hostname
const char *host_name = "echo.u-blox.com";

// Echo server TCP port
const int port = 7;

/**
 * Connects to the Cellular Network
 */
nsapi_error_t do_connect()
{
    nsapi_error_t retcode;
    uint8_t retry_counter = 0;

    while (!iface.is_connected()) {

        retcode = iface.connect();
        if (retcode == NSAPI_ERROR_AUTH_FAILURE) {
            printf("\n\nAuthentication Failure. Exiting application\n");
            return retcode;
        } else if (retcode != NSAPI_ERROR_OK) {
            printf("\n\nCouldn't connect: %d, will retry\n", retcode);
            retry_counter++;
            continue;
        } else if (retcode != NSAPI_ERROR_OK && retry_counter > RETRY_COUNT) {
            printf("\n\nFatal connection failure: %d\n", retcode);
            return retcode;
        }

        break;
    }

    printf("\n\nConnection Established.\n");

    return NSAPI_ERROR_OK;
}

/**
 * Opens a TCP socket with the given echo server and undegoes an echo
 * transaction.
 */
nsapi_error_t test_send_recv()
{
    nsapi_size_or_error_t retcode;

    TCPSocket sock;

    retcode = sock.open(&iface);
    if (retcode != NSAPI_ERROR_OK) {
        printf("TCPSocket.open() fails, code: %d\n", retcode);
        return -1;
    }

    SocketAddress sock_addr;
    retcode = iface.gethostbyname(host_name, &sock_addr);
    if (retcode != NSAPI_ERROR_OK) {
        printf("Couldn't resolve remote host: %s, code: %d\n", host_name,
               retcode);
        return -1;
    }

    sock_addr.set_port(port);

    sock.set_timeout(15000);
    int n = 0;
    char *echo_string = "TEST";
    char recv_buf[4];

    retcode = sock.connect(sock_addr);
    if (retcode < 0) {
        printf("TCPSocket.connect() fails, code: %d\n", retcode);
        return -1;
    } else {
        printf("TCP: connected with %s server\n", host_name);
    }
    retcode = sock.send((void*) echo_string, sizeof(echo_string));
    if (retcode < 0) {
        printf("TCPSocket.send() fails, code: %d\n", retcode);
        return -1;
    } else {
        printf("TCP: Sent %d Bytes to %s\n", retcode, host_name);
    }

    n = sock.recv((void*) recv_buf, sizeof(recv_buf));

    sock.close();

    if (n > 0) {
        printf("Received from echo server %d Bytes\n", n);
        return 0;
    }

    return -1;

    return retcode;
}

int main()
{
    iface.modem_debug_on(MBED_CONF_APP_MODEM_TRACE);
    /* Set Pin code for SIM card */
    iface.set_sim_pin(PIN_CODE);

    /* Set network credentials here, e.g., APN*/
    iface.set_credentials(CREDENTIALS);

    printf("\n\nmbed-os-example-cellular, Connecting...\n");

    /* Attempt to connect to a cellular network */
    if (do_connect() == NSAPI_ERROR_OK) {
        nsapi_error_t retcode = test_send_recv();
        if (retcode == NSAPI_ERROR_OK) {
            printf("\n\nSuccess. Exiting \n\n");
            return 0;
        }
    }

    printf("\n\nFailure. Exiting \n\n");
    return -1;
}
// EOF
```
