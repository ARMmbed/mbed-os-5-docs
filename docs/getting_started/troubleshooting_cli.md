 
## Troubleshooting with mbed CLI

### Unable to import Mercurial (mbed.org) programs or libraries.
1. Check whether you have Mercurial installed in your system path by  running `hg` in command prompt. If you're receiving "command not found" or a similar message, then you need to install Mercurial, and add it to your system path.

2. Try to clone a Mercurial repository directly. For example, `hg clone https://developer.mbed.org/teams/mbed/code/mbed_blinky/`. If you receive an error similar to `abort: error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.:590)`, then your system certificates are out of date. You need to update your system certificates and possibly add the host certificate fingerprint of `mbed.com` and `mbed.org`. Read more about Mercurial's certificate management [here](https://www.mercurial-scm.org/wiki/CACertificates).

### Various issues when running mbed CLI in Cygwin environment
Currently mbed CLI is not compatible with Cygwin environment and cannot be executed inside it (https://github.com/ARMmbed/mbed-cli/issues/299).
