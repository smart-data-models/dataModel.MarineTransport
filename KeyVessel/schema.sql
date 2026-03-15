/* (Beta) Export of data model KeyVessel of the subject dataModel.MarineTransport 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE dataProvider_type AS ENUM ('AIS', 'AISHUB', 'ALGORITHM', 'IA', 'MARINETRAFFIC');
CREATE TYPE navigationStatus_type AS ENUM ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15');
CREATE TYPE positionAccuracy_type AS ENUM ('0', '1');
CREATE TYPE KeyVessel_type AS ENUM ('KeyVessel');

CREATE TABLE KeyVessel (
    address JSON,
    alternateName TEXT,
    areaServed TEXT,
    callSign TEXT,
    courseOverGround NUMERIC,
    createdDate TIMESTAMP,
    dataProvider dataProvider_type,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    deletedDate TIMESTAMP,
    description TEXT,
    etaAis TIMESTAMP,
    etaAlgorithm TIMESTAMP,
    flagCode TEXT,
    id TEXT PRIMARY KEY,
    imo NUMERIC,
    lastPortCode TEXT,
    latitude NUMERIC,
    longitude NUMERIC,
    mmsi NUMERIC,
    modifiedDate TIMESTAMP,
    name TEXT,
    navigationStatus navigationStatus_type,
    nextPortCode TEXT,
    observedDate TIMESTAMP,
    owner JSON,
    portCallNumber TEXT,
    portCallRef TEXT,
    portCode TEXT,
    positionAccuracy positionAccuracy_type,
    seeAlso JSON,
    source TEXT,
    speedOverGround NUMERIC,
    type KeyVessel_type,
    vesselAtPort BOOLEAN,
    vesselName TEXT,
    vesselRef TEXT
);