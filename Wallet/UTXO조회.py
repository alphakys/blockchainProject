import requests

#아래의 주소의 UTXO를 조회한다.

addr = '1Nh7uHdvY6fNwtQtM1G5EZAFPLC33B59rB'
url = 'https://blockchain.info/unspent?active=' + addr
resp = requests.get(url=url)
if resp.status_code != 200:
        print("\n", resp.text)
else:
    data = resp.json()
    utxo = data['unspent_outputs']

#UTXO가 여러 개인 경우 모두 출력한다.
totBalance = 0;
print("\nNumber of UTXOs = ", len(utxo))
for n in range(len(utxo)):
    print("Confirmations=", utxo[n]['confirmations'])
    print("tx_hash= ", utxo[n]['tx_hash'])
    print("tx_output_n= ", utxo[n]['tx_output_n'])
    print("value = ", utxo[n]['value'])
    print()
    totBalance += utxo[n]['value']

    #UTXO value의 총합이 이 지갑에서 사용할 수 있는 총 잔액임
    print("\nTotal Balnace = ", totBalance, '(Satoshi)')




