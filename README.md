1. Get python

https://github.com/pyenv/pyenv
```bash
brew install pyenv
pyenv install 3.9.6
pyenv versions
```

~/.zprofile
```bash
eval "$(pyenv init --path)"
```

```bash
pyenv global 3.9.6
```

2. Install Pip

https://pip.pypa.io/en/stable/installation/

```bash
sudo python -m ensurepip --upgrade
sudo pip install --upgrade pip
```

3. Create bg

```python
data = np.random.random((191, 1128))
Image.fromarray(data,'RGB').save("output.png")
```
