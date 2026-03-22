/* (Beta) Export of data model Terminal of the subject dataModel.MarineTransport 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Terminal_type AS ENUM ('Terminal');

CREATE TABLE Terminal (
    address JSON,
    alternateName TEXT,
    areaServed TEXT,
    code TEXT,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    description TEXT,
    id TEXT PRIMARY KEY,
    location JSON,
    mrn TEXT,
    name TEXT,
    owner JSON,
    portCode TEXT,
    remarks TEXT,
    seeAlso JSON,
    source TEXT,
    tafTsiLocationCode TEXT,
    terminal TEXT,
    type Terminal_type
);