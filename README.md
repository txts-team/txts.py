# txts.py
*Python wrapper for interacting with [txts](https://https://github.com/txts-team/txts)*
## Contributing

This project is very much work in progress, any contributions would be appreciated<br>
If you make a pull request please use proper tags and follow the contributor [Code Of Conduct](https://github.com/txts-team/txts.py/blob/master/CODE_OF_CONDUCT.md)

## Installing

```
python3 -m pip install -U txts
```

## Simple Example

```python
import txts

instance = txts.TxtInstance('instance_url')
print(instance.Status())
try:
    instance.EditPage('username','secret','content')
    print('Sucessfully updated page!')
except
    print('Failed to update page!')
```    

## Links

[Txts Discord]()<br>
[Txts official instance](https://txts.sudokoko.xyz/)