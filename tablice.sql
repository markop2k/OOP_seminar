CREATE TABLE korisnik (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    korisnicko_ime VARCHAR(100) NOT NULL,
    lozinka VARCHAR(100) NOT NULL,
    ime VARCHAR(100) NOT NULL,
    prezime VARCHAR(100) NOT NULL,
    saldo DECIMAL(10, 2) NOT NULL
 );

CREATE TABLE dobitak (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    korisnicko_ime VARCHAR(100) NOT NULL,
    ime_kategorije VARCHAR(100) NOT NULL,
    datum DATE,
    dobitak DECIMAL(10, 2) NOT NULL,
    tip VARCHAR(10) NOT NULL
 );

CREATE TABLE trosak (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    korisnicko_ime VARCHAR(100) NOT NULL,
    ime_kategorije VARCHAR(100) NOT NULL,
    datum DATE,
    trosak DECIMAL(10, 2) NOT NULL,
    tip VARCHAR(10) NOT NULL
 );

INSERT INTO korisnik (korisnicko_ime, lozinka, ime, prezime, saldo)
    VALUES ('Parko', 'www', 'Marko', 'P', 7);

INSERT INTO dobitak (korisnicko_ime, ime_kategorije, datum, dobitak, tip)
    VALUES ('Parko', 'Placa', 1999-02-01, 10.12, 'dobitak');
INSERT INTO trosak (korisnicko_ime, ime_kategorije, datum, trosak, tip)
    VALUES ('Parko', 'Racuni', 2020-07-03, 20.99, 'trosak');
INSERT INTO dobitak (korisnicko_ime, ime_kategorije, datum, dobitak, tip)
    VALUES ('Parko', 'Prodaja', 2024-11-05, 4.10, 'dobitak');
