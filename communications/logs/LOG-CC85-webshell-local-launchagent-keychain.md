# LOG-CC85 webshell local launchagent keychain

## Intent

Promote webshell from manual terminal runtime to always-on local operator service with Keychain-backed secret injection.

## Shipped

1. keychain helper:
   - [webshell_keychain.sh](/Users/system/syncrescendence/operators/webshell/webshell_keychain.sh)
2. launchagent runner:
   - [webshell_launchagent_runner.sh](/Users/system/syncrescendence/operators/webshell/webshell_launchagent_runner.sh)
3. launchagent installer/status:
   - [install_local_webshell_launchagent.sh](/Users/system/syncrescendence/operators/webshell/install_local_webshell_launchagent.sh)
   - [webshell_launchagent_status.sh](/Users/system/syncrescendence/operators/webshell/webshell_launchagent_status.sh)
4. launchagent plist:
   - [com.syncrescendence.webshell-ops.plist](/Users/system/syncrescendence/orchestration/state/impl/com.syncrescendence.webshell-ops.plist)
5. env-secret fallback added to:
   - [syncrescendence_dev_shell.py](/Users/system/syncrescendence/operators/webshell/syncrescendence_dev_shell.py)
6. make targets added:
   - `webshell-keychain-status`
   - `webshell-keychain-init-callback`
   - `webshell-launchagent-install`
   - `webshell-launchagent-status`
   - `webshell-launchagent-restart`

## Operational result

Webshell can run persistently without embedding callback/provider secrets in CLI invocation strings.

## Verification checklist

1. `python3 -m py_compile operators/webshell/syncrescendence_dev_shell.py`
2. `bash -n operators/webshell/webshell_keychain.sh`
3. `bash -n operators/webshell/webshell_launchagent_runner.sh`
4. `bash -n operators/webshell/install_local_webshell_launchagent.sh`
5. `bash -n operators/webshell/webshell_launchagent_status.sh`
6. `make check-artifact-law`
