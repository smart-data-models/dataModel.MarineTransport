<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: PortCall  
================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/PortCall/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **포트 콜이란 선박이 화물의 적재 또는 하역과 같은 유용한 기능을 수행하기 위해 일정 기간 동안 항구를 방문하는 것을 말합니다.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `UNLOCODE[string]`: 해당 항구의 유엔 무역 및 운송 위치 코드, [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예: 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDate[date-time]`: 선박이 항구 지역에 도착하는 날짜/시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `arrivalDateScheduled[date-time]`: 배송업체가 신고한 선박의 항구 지역 도착 예정 날짜/시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자열입니다.  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `departureDate[date-time]`: 선박이 항구 지역을 떠나는 날짜/시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `departureDateScheduled[date-time]`: 선박이 항구 지역에서 출발할 예정 날짜/시간(운송업체가 신고한 날짜/시간)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `regularLine[string]`: 포트콜의 일반 회선  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 일련의 문자입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `status[string]`: 작업의 상태입니다. 열거형: '예상, 승인됨, 운영 중, 완료됨'  - `terminal[string]`: 포트콜의 터미널  - `type[string]`: NGSI 엔티티 유형. PortCall이어야 합니다.  - `vessel[object]`: 포트콜의 호출 선박  	- `IMO[number]`: 국제해사기구에서 정의한 [체계](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx)에 따른 IMO 선박 식별 번호입니다.    
	- `shipName[string]`: 선박 이름    
	- `shipTypeCategory[string]`: 선박 카테고리에 대한 설명. Enum: '컨테이너, 일반 화물 비특수, 액체 벌크, 건식 벌크, 크루즈'    
	- `shipTypeClass[string]`: 선박 등급 설명. 열거형: '멀티데커, 케미컬 탱커, 풀 컨테이너, 오일 탱커, 벌크 캐리어, LG 탱커'    
- `vesselAgent[string]`: 포트콜의 선박 에이전트  - `voyageCode[string]`: 항해 코드(항해의 고유 ID)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `arrivalDate`  - `id`  - `type`  - `vessel`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
H2020 프로젝트 데이터포트의 데이터 모델입니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PortCall:    
  description: 'A Port Call is a vessel''s visit to the port for a period of time, in order to perform some kind of useful function, like the loading or unloading of goods.'    
  properties:    
    UNLOCODE:    
      description: 'United Nations Code for Trade and Transport Locations, [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory), of the port'    
      type: string    
      x-ngsi:    
        type: Property    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    arrivalDate:    
      description: Date/time of ship arrival at port area    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    arrivalDateScheduled:    
      description: 'Scheduled date/time of ship arrival at port area, as declared by shipping agent'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    departureDate:    
      description: Date/time of ship leaving port area    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    departureDateScheduled:    
      description: 'Scheduled date/time of ship leaving port area, as declared by shipping agent'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    regularLine:    
      description: Regular line of the portcall    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Status of the operation. Enum: ''Estimated, Authorized, Operational, Completed'''    
      enum:    
        - Estimated    
        - Authorized    
        - Operational    
        - Completed    
      type: string    
      x-ngsi:    
        type: Property    
    terminal:    
      description: Terminal of the portcall    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PortCall    
      enum:    
        - PortCall    
      type: string    
      x-ngsi:    
        type: Property    
    vessel:    
      description: Calling vessel of the portcall    
      properties:    
        IMO:    
          description: 'IMO ship identification number, following the [scheme](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) defined by the International Maritime Organization.'    
          type: number    
          x-ngsi:    
            type: Property    
        shipName:    
          description: Name of the vessel    
          type: string    
          x-ngsi:    
            type: Property    
        shipTypeCategory:    
          description: 'Description of vessel category. Enum: ''CONTAINER, GENERAL CARGO NON SPECIALIZED, LIQUID BULK, DRY BULK, CRUISE'''    
          enum:    
            - CONTAINER    
            - GENERAL CARGO NON SPECIALIZED    
            - LIQUID BULK    
            - DRY BULK    
            - CRUISE    
          type: string    
          x-ngsi:    
            type: Property    
        shipTypeClass:    
          description: 'Description of vessel class. Enum: ''MULTI-DECKER, CHEMICAL TANKER, FULL CONTAINER, OIL TANKER, BULK CARRIER, LG TANKER'''    
          enum:    
            - MULTI-DECKER    
            - CHEMICAL TANKER    
            - FULL CONTAINER    
            - OIL TANKER    
            - BULK CARRIER    
            - LG TANKER    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    vesselAgent:    
      description: Vessel Agent of the portcall    
      type: string    
      x-ngsi:    
        type: Property    
    voyageCode:    
      description: Voyage code (unique ID of a voyage)    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - vessel    
    - arrivalDate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/PortCall/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/PortCall/schema.json    
  x-model-tags: i4trust    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### PortCall NGSI-v2 키-값 예시  
다음은 JSON-LD 형식의 키 값으로 된 PortCall의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": "ESVLC",  
  "arrivalDate": "2021-12-01T00:46:00Z",  
  "arrivalDateScheduled": "2021-12-01T00:46:00Z",  
  "departureDate": "2021-12-01T11:35:00Z",  
  "departureDateScheduled": "2021-12-01T11:35:00Z",  
  "regularLine": "GRIMALDI - SHORT SEA SERVICE B",  
  "status": "Completed",  
  "terminal": "VALENCIA TERMINAL EUROPA, S.A.",  
  "vessel": {  
    "shipName": "ECO BARCELONA",  
    "IMO": 8712345,  
    "shipTypeCategory": "CONTAINER",  
    "shipTypeClass": "FULL CONTAINER"  
  },  
  "vesselAgent": "GRIMALDI LOGISTICA ESPA\u00d1A S.L.",  
  "voyageCode": "1202106029"  
}  
```  
</details>  
#### PortCall NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PortCall의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": {  
    "type": "Text",  
    "value": "ESVLC",  
    "metadata": {}  
  },  
  "arrivalDate": {  
    "type": "DateTime",  
    "value": "2021-12-01T00:46:00Z",  
    "metadata": {}  
  },  
  "arrivalDateScheduled": {  
    "type": "DateTime",  
    "value": "2021-12-01T00:46:00Z",  
    "metadata": {}  
  },  
  "departureDate": {  
    "type": "DateTime",  
    "value": "2021-12-01T11:35:00Z",  
    "metadata": {}  
  },  
  "departureDateScheduled": {  
    "type": "DateTime",  
    "value": "2021-12-01T11:35:00Z",  
    "metadata": {}  
  },  
  "regularLine": {  
    "type": "Text",  
    "value": "GRIMALDI - SHORT SEA SERVICE B",  
    "metadata": {}  
  },  
  "status": {  
    "type": "Text",  
    "value": "Completed",  
    "metadata": {}  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "VALENCIA TERMINAL EUROPA, S.A.",  
    "metadata": {}  
  },  
  "vessel": {  
    "type": "StructuredValue",  
    "value": {  
      "shipName": "ECO BARCELONA",  
      "IMO": 8712345,  
      "shipTypeCategory": "CONTAINER",  
      "shipTypeClass": "FULL CONTAINER"  
    },  
    "metadata": {}  
  },  
  "vesselAgent": {  
    "type": "Text",  
    "value": "GRIMALDI LOGISTICA ESPA\u00d1A S.L.",  
    "metadata": {}  
  },  
  "voyageCode": {  
    "type": "Text",  
    "value": "1202106029",  
    "metadata": {}  
  }  
}  
```  
</details>  
#### PortCall NGSI-LD 키-값 예시  
다음은 JSON-LD 형식의 키 값으로 된 PortCall의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": "ESVLC",  
  "arrivalDate": "2021-12-01T00:46:00Z",  
  "arrivalDateScheduled": "2021-12-01T00:46:00Z",  
  "departureDate": "2021-12-01T11:35:00Z",  
  "departureDateScheduled": "2021-12-01T11:35:00Z",  
  "regularLine": "GRIMALDI - SHORT SEA SERVICE B",  
  "status": "Completed",  
  "terminal": "VALENCIA TERMINAL EUROPA, S.A.",  
  "vessel": {  
    "shipName": "ECO BARCELONA",  
    "IMO": 8712345,  
    "shipTypeCategory": "CONTAINER",  
    "shipTypeClass": "FULL CONTAINER"  
  },  
  "vesselAgent": "GRIMALDI LOGISTICA ESPA\u00d1A S.L.",  
  "voyageCode": "1202106029",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PortCall NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PortCall의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "arrivalDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-12-01T00:46:00Z"  
    }  
  },  
  "arrivalDateScheduled": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-12-01T00:46:00Z"  
    }  
  },  
  "departureDate": {  
    "type": "Property",  
    "value": "2021-12-01T11:35:00Z",  
    "metadata": {}  
  },  
  "departureDateScheduled": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-12-01T11:35:00Z"  
    }  
  },  
  "regularLine": {  
    "type": "Property",  
    "value": "GRIMALDI - SHORT SEA SERVICE B"  
  },  
  "status": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "VALENCIA TERMINAL EUROPA, S.A."  
  },  
  "vessel": {  
    "type": "Property",  
    "value": {  
      "shipName": "ECO BARCELONA",  
      "IMO": 8712345,  
      "shipTypeCategory": "CONTAINER",  
      "shipTypeClass": "FULL CONTAINER"  
    }  
  },  
  "vesselAgent": {  
    "type": "Property",  
    "value": "GRIMALDI LOGISTICA ESPAÃ‘A S.L."  
  },  
  "voyageCode": {  
    "type": "Property",  
    "value": "1202106029"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
크기 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
