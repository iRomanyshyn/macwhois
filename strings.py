# Strings file for macwhois

hello = """Hi! This tool is used to identify network device's manufacturer by it's unique (in most cases) MAC address. 
It using IEEE OUI database information to find first three octets (24 bits) of MAC address provided in OUI database.

You can search MAC addresses like this:

    112233445566        (without any other symbols);
    11-22-33-44-55-66   (with dash after every two chars);
    11:22:33:44:55:66   (with semicolons after every two chars);
    1122.3344.5566      (with dot after every four chars);
    1122-3344-5566      (with dash after every four chars).

You can search as many MACs as you want by passing them as command line parameters with spaces between it:

macwhois [MAC1] [MAC2] [...] [MACn]

or you can try to provide it ouidata file with MAC addresses which contains MAC addresses separated by spaces or newlines:

macwhois $(cat [file.txt])

You can use it interactively while started with -i argument.

Exit codes: 0 = OK, 1 = can't open data source."""

downloading = "Downloading fresh OUI file..."

fail_download = "Error while trying to get fresh IEEE OUI file:"

fail_open = "Can't open local OUI data:"

fail_all = "Failed to open both local and remote data. We can't use any data source, so we can only exit."