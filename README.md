
# Bukalapak Scrapping dengan Laravel & Python

Sebuah source code yang berisi tentang api dari scrapping data bukalapak dengan menggunakan bahasa python dan php (Laravel).


## API Documentation

#### GET SEARCH

```http
  GET /api/search
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `q` | `string` | **Wajib**. Benda yang dicari |



## Deployment

Untuk pake API ini caranya pertama:

```bash
  python resources/plugins/setup.py
```

Lalu jalankan perintah ini:

```bash
  composer install
  php artisan serve
```

Enjoy!

## Note

API ini masih dalam tahap pengembangan dan masih belum final. 

