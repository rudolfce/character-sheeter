## Migração

Para aplicar as migrações:
```bash
$ FLASK_APP=app.py flask db upgrade
```

Para criar migrações a partir do novo estado

## Manipulação de dados

```python
from app import app
from sheeter.database import db


with app.app_context():
    session = db.Session()
    # Do stuff
```