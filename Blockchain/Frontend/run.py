""" 
Copyright (c) 2021 Codiesalert.com
These scripts should be used for commercial purpose without Codies Alert Permission
Any violations may lead to legal action
"""
from flask import Flask, render_template, request
from Blockchain.client.sendBTC import SendBTC
from Blockchain.Backend.core.Tx import Tx

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def wallet():
    message = ""
    if request.method == "POST":
        FromAddress = request.form.get("fromAddress")
        ToAddress = request.form.get("toAddress")
        Amount = request.form.get("Amount", type=int)
        sendCoin = SendBTC(FromAddress, ToAddress, Amount, UTXOS)
        TxObj = sendCoin.prepareTransaction()

        scriptPubKey = sendCoin.scriptPubKey(FromAddress)
        verified = True

        if not TxObj:
            message = "Invalid Transaction"

        if isinstance(TxObj, Tx):
            for index, tx in enumerate(TxObj.tx_ins):
                if not TxObj.verify_input(index, scriptPubKey):
                    verified = False

            if verified:
                MEMPOOL[TxObj.TxId] = TxObj
                message = "Transaction added in memory Pool"

    return render_template("wallet.html", message=message)


def main(utxos, MemPool):
    global UTXOS
    global MEMPOOL
    UTXOS = utxos
    MEMPOOL = MemPool
    app.run()
