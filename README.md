1. Get python

https://github.com/pyenv/pyenv
```
brew install pyenv
pyenv install 3.9.6
pyenv versions
```

~/.zprofile
```
eval "$(pyenv init --path)"
```

```
pyenv global 3.9.6
```

2. Install Pip

https://pip.pypa.io/en/stable/installation/

```
sudo python -m ensurepip --upgrade
sudo pip install --upgrade pip
```

3. Create bg

```
data = np.random.random((191, 1128))
Image.fromarray(data,'RGB').save("output.png")
```
