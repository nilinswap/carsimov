# carsimov

#### create virtualenv

-`pyenv virtualenv 3.7.4 v_name`
- `pyenv activate v_name`

#### Run app
- `python src/server.py`

#### Caveats
- when working in flask, css files are included in html as follows
```html 
<link rel="stylesheet" type="text/css" href= "{{ url_for('static',filename='styles/map.css') }}">
```