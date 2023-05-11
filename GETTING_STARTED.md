# Getting Started

There are multiple ways to get started with Findy Test Net.

## Use an existing Wallets
Findy Test Net is pre-registered at least in the following wallet implementations:
* iGrant Data Wallet
  * [App Store](https://apple.co/2Mz9nJp)
  * [Google Play](https://play.google.com/store/apps/details?id=io.igrant.mobileagent)
* Lissi Agent
  * [App Store](https://apps.apple.com/en/app/lissi-wallet/id1529848685)
  * [Google Play](https://play.google.com/store/apps/details?id=io.lissi.mobile.android)

## Access the ledger via Indy SDK
### Install Indy SDK
* [Getting started with Docker](https://hyperledger-indy.readthedocs.io/projects/sdk/en/latest/docs/getting-started/run-getting-started.html)
* [Building Indy SDK](https://hyperledger-indy.readthedocs.io/projects/sdk/en/latest/docs/build-guides/index.html)
* [Indy SDK wrapper for iOS development](https://hyperledger-indy.readthedocs.io/projects/sdk/en/latest/wrappers/ios/README.html)

Download FindyTestNet genesis file from the management portal (Genesis-link in the left-hand side navigation) and store it to a folder on the device you're running Indy SDK on.
```sh
mkdir ~/FindyTestNet
mv ~/Downloads/findy_genesis.json ~/FindyTestNet
cd ~/FindyTestNet
indy-cli
```

```
indy> pool create FindyTestNet gen_txn_file=findy_genesis.json
indy> wallet create MyTestWallet key
```

## ACA-py
Coming later...

## Aries Javascript Framework (v0.3)
* Download FindyTestNet genesis file from the management portal (Genesis-link in the left-hand side navigation) and store it as `constants/findy_genesis.json` in your project folder.
* Create a wallet configuration:
```js
  walletConfig: {
    id: 'MyTestWallet',
    key: '********************************', // replace with your own key
    // ...
  },
  indyLedgers: [
    {
      id: 'FindyTestNet',
      indyNamespace: 'findy',
      isProduction: false,
      genesisPath: './constants/findy_genesis.json',
      // ...
    },
  ],
```

## Indy Story Walkthrough (a Developer Guide for Building Indy Clients Using Libindy)
You should be able to execute the whole [Indy Story Walkthrough](https://hyperledger-indy.readthedocs.io/projects/sdk/en/latest/docs/getting-started/indy-walkthrough.html).
Use the Steward DID you received when signing up to the network to create Verinyms for Faber College, Acme Corp and Thrift bank. The step 3 in the walkthrough has already been done and you should have your `steward['did']` and `steward['key']`. You can continue from step 4 but please do read the first chapters to understand what's going on.
