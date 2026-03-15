/* (Beta) Export of data model Metocean of the subject dataModel.MarineTransport 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Metocean_type AS ENUM ('Metocean');

CREATE TABLE Metocean (
    address JSON,
    alternateName TEXT,
    areaServed TEXT,
    code TEXT,
    collectionName TEXT,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    description TEXT,
    fromDate TIMESTAMP,
    id TEXT PRIMARY KEY,
    location JSON,
    modifiedAt TIMESTAMP,
    name TEXT,
    owner JSON,
    points JSON,
    seeAlso JSON,
    source TEXT,
    toDate TIMESTAMP,
    type Metocean_type
);