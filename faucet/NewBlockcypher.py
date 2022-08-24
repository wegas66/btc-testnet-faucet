from pycoin.services.blockcypher import *


class NewBlockcypherProvider(BlockcypherProvider):

    def spendables_for_address(self, address):
        """
        Return a list of Spendable objects for the
        given bitcoin address.
        """
        spendables = []
        url_append = "?unspentOnly=true&includeScript=true"
        url = self.base_url("addrs/%s%s" % (address, url_append))
        result = json.loads(urlopen(url).read().decode("utf8"))
        for txn in result.get("txrefs", []):
            coin_value = txn.get("value")
            script = h2b(txn.get("script"))
            previous_hash = h2b_rev(txn.get("tx_hash"))
            previous_index = txn.get("tx_output_n")
            spendables.append(Tx.Spendable(coin_value, script, previous_hash, previous_index))
        return spendables
