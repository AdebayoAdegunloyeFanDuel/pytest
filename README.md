**`Documentation`**

This is a quick overview of pytest.
The tests are wrriten in python 3.

To ensure you can run the test.
First install pytest.
`pip install pytest`

Then `cd` into the directory.
There are few way to run pyest, which are:

`pytest` 
`pytest -v` 
`pytest -q`
`pytest -v -k {specific text}`

The test is testing against a wallet applicate.
The guy only guy started with 20 in his wallet
and sometimes broke (meaning got no money).

The test test agaist to make sure this broke dude can not withdrawal more than he has
and when he add money into his wallet then it does add up.



