<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 엔티티: MasterVessel  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **데이터 모델은 선박에 대한 정보를 제공하기 위한 것입니다. 각 선박의 속성(정적 및 동적 정보**)을 나타낼 수 있습니다.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: 선박의 빔  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildDate[date]`: ISO 8601 UTC 형식으로 표시되는 선박의 건조 날짜  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: 무선으로 최초 연결 시 선박의 식별 신호 [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: 호출명 / 호출 부호] [IMO: IMO0136].  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `dwt[number]`: 재화중량톤수(DWT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `financialOwner[string]`: 선박의 금융 소유자  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: 국제 국기 코드(ISO 3166-1 알파-2)  . Model: [https://schema.org/Text](https://schema.org/Text)- `gt[number]`: 총 톤수(GT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `imo[number]`: 국제 해사기구 번호(글로벌 영구 UID) [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140]  . Model: [https://schema.org/Number](https://schema.org/Number)- `loa[number]`: 용기 전체에 걸친 길이  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `manager[string]`: 선박 관리자, 일반적으로 선박 회사  . Model: [https://schema.org/Text](https://schema.org/Text)- `maxDraught[number]`: 선박의 최대 흘수  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLoadVehicle[number]`: 차량을 운송할 수 있는 선박의 최대 용량  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPassenger[number]`: 승객을 수송할 수 있는 선박의 최대 수용 인원  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVehicle[number]`: 허용되는 차량의 최대 크기  . Model: [https://schema.org/Number](https://schema.org/Number)- `minNumOfCrew[number]`: 선박 운항을 위한 최소 승무원 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: 해양 모바일 서비스 식별 번호(해당 개체의 현재 기국 상태에 의해 임시로 할당된 UID)[EMSWe: DE-068-09] [EDIFACT: TDT-1131] [IALA_S211:vesselId] [IMO: IMO0178] [IMO: IMO0178]  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `photo[uri]`: 선박 사진 URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `sleeve[number]`: 용기 슬리브  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `technicalManager[string]`: 선박의 기술 관리자  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: 활 치수  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: 치수에서 포트까지  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: 우현 치수  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: 선미까지의 치수  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI 엔티티 유형. 마스터비셀이어야 합니다.  - `vesselClass[string]`: 선박 등급 코드. Enum:'BD=건화물선; BO=유조선/벌크선; BS=벌크선 하역; BY=기타 유형의 벌크선; FC=어선; FO=선박. 환적 및/또는 운송; GA=선박. 승객을 태운 RO-RO; GC=특수화되지 않은 일반 화물선; GD=일반 화물선; GE=복합 운송; GN=컨테이너선; GO=로로선; GP=여객선; GR=냉동선; OO=부유물 또는 인공물; OS=공급선; TC=운송 제품. 화학물질; TD=기타 액체 벌크; TL=액화 가스 운송; TO=유조선; XD=준설선; XR=연구 및 탐사; XT=예인선 / 푸셔; XX=기타 선박 및 보트; UR=패스트 패스; G=일반 화물; T=액체 벌크선(탱크); S=고체 벌크선; OB=기타 상선; UC=크루즈 티켓; OC=공해어선(냉동선); '  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselName[string]`: 선박 이름. [EMSWe: DE-003-07] [EDIFACT: TDT-8212] [IMO: IMO0142]  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselOwner[string]`: 선박 소유자  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselSubType[number]`: Enum:'0=사용 불가(기본값),1-19=향후 사용을 위해 예약됨,20=지상 착륙(WIG), 이 유형의 모든 선박,21=지상 착륙(WIG), 위험 범주 A,22=지상 착륙(WIG), 위험 범주 B,23=지상정박(WIG), 위험 범주 C,24=지상정박(WIG), 위험 범주 D,25-29=지상정박(WIG), 향후 사용 예약,30=어업,31=예인,32=예인: 길이 200m 초과 또는 폭 25m 초과,33=준설 또는 수중 작업,34=잠수 작업,35=군사 작전,36=항해,37=유람선,38-39=예약,40=고속선(HSC), 이 유형의 모든 선박,41=고속선(HSC), 위험 범주 A,42=고속선(HSC), 위험 범주 B,43=고속선(HSC), 위험 범주 C,44=고속선박(HSC), 위험 범주 D,45-48=고속선박(HSC), 향후 사용 예약,49=고속선박(HSC), 추가 정보 없음,50=도선선,51=수색 및 구조선,52=예인선,53=항만 입찰,54=오염 방지 장비,55=법 집행,56-57=스페어 - 지역 선박,58=의료 수송,59=RR 결의 번호에 따른 비전투원 선박. 18,60=여객, 이 유형의 모든 선박,61=여객, 위험 범주 A,62=여객, 위험 범주 B,63=여객, 위험 범주 C,64=여객, 위험 범주 D,65-68=여객, 향후 사용을 위해 예약,69=여객, 추가 정보 없음,70=화물, 이 유형의 모든 선박,71=화물, 위험 범주 A,72=화물, 위험 범주 B,73=화물, 위험 범주 C,74=화물, 위험 범주 D,75-78=화물, 향후 사용을 위해 예약,79=화물, 추가 정보 없음,80=탱커, 이 유형의 모든 선박,81=탱커, 위험 범주 A,82=탱커, 위험 범주 B,83=탱커, 위험 범주 C,84=탱커, 위험 범주 D,85-88=탱커, 향후 사용을 위해 예약,89=탱커, 추가 정보 없음,90=기타 유형, 이 유형의 모든 선박,91=기타 유형, 위험 범주 A,92=기타 유형, 위험 범주 B,93=기타 유형, 위험 범주 C,94=기타 유형, 위험 범주 D,95-98=기타 유형, 향후 사용을 위해 예약,99=기타 유형, 추가 정보 없음'. 선박 하위 유형 코드  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: Enum:'1=예약,2=육상,3=특수 범주,4=고속선박,5=특수 범주,6=여객,7=화물,8=탱커,9=기타'. 선박 유형 코드  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MasterVessel:    
  description: 'The data model is intended to provide information about vessels. It allows to represent the properties of each vessel: static and dynamic information'    
  properties:    
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
    beam:    
      description: Beam of the Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    buildDate:    
      description: Date of building of the vessel represented by an ISO 8601 UTC format    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    callSign:    
      description: 'Identification signal of a vessel when initially connecting by radio [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Call Name / Call Sign] [IMO: IMO0136] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dwt:    
      description: Dead weight Tonnage (DWT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: tons    
    financialOwner:    
      description: Financial Owner of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: International Flag Code (ISO 3166-1 alfa-2)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    gt:    
      description: Gross Tonnage (GT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: moorson tons    
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
        type: Relationship    
    imo:    
      description: 'International Maritime Organization Number (a global forever UID) [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140] '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    loa:    
      description: Length Over All of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
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
    manager:    
      description: 'Manager of the Vessel, usually Ship Company'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    maxDraught:    
      description: Maximum Draught of the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    maxLoadVehicle:    
      description: Max capacity of vessel to transport vehicles    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxPassenger:    
      description: Max capacity of vessel to transport passengers    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVehicle:    
      description: Max dimensions of vehicle permitted    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minNumOfCrew:    
      description: Minimum number of crew to operate the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mmsi:    
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    photo:    
      description: Vessel Photo URL    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    sleeve:    
      description: Sleeve of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    technicalManager:    
      description: Technical Manager of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toBow:    
      description: Dimension to Bow    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toPort:    
      description: Dimension to Port    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStardboard:    
      description: Dimension to Starboard    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStern:    
      description: Dimension to Stern    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    type:    
      description: NGSI Entity type. It has to be MasterVessel    
      enum:    
        - MasterVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselClass:    
      description: 'Code for vessel class. Enum:''BD=Dry bulk; BO=Oil tanker / bulk carrier; BS=Bulk carrier unloading; BY=Other types of bulk carriers; FC=Fishing vessel; FO=Vessel. transfer and/or transp.; GA=Vessel. RO-RO with passengers; GC=Mrcia general without specialization; GD=Rest general cargo vessels; GE=Buq. transp. combined; GN=Container ship; GO=Ro-ro vessel; GP=Passenger ship; GR=Refrigerator vessel; OO=Buq. or artefact. float be; OS=Supply ships; TC=Transport product. chemicals; TD=Other liquid bulk; TL=Transportation of liquefied gas; TO=Oil tanker; XD=Dredges; XR=Research and exploration; XT=Tugs / pushers; XX=Other ships and boats; UR=Fast Pass; G=General Cargo; T=Liquid Bulk Carriers (Tanks); S=Solid Bulk Carriers; OB=Other Merchant Vessels; UC=Cruise Ticket; OC=High Sea Fishing Vessels (Freezers);'''    
      enum:    
        - BD    
        - BO    
        - BS    
        - BY    
        - FC    
        - FO    
        - GA    
        - GC    
        - GD    
        - GE    
        - GN    
        - GO    
        - GP    
        - GR    
        - OO    
        - OS    
        - TC    
        - TD    
        - TL    
        - TO    
        - XD    
        - XR    
        - XT    
        - XX    
        - UR    
        - G    
        - T    
        - S    
        - OB    
        - UC    
        - OC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselName:    
      description: 'Name of the Vessel. [EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselOwner:    
      description: Owner of the Vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselSubType:    
      description: 'Enum:''0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information''. Code for vessel Sub-Type'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 13    
        - 14    
        - 15    
        - 16    
        - 17    
        - 18    
        - 19    
        - 20    
        - 21    
        - 22    
        - 23    
        - 24    
        - 25    
        - 26    
        - 27    
        - 28    
        - 29    
        - 30    
        - 31    
        - 32    
        - 33    
        - 34    
        - 35    
        - 36    
        - 37    
        - 38    
        - 39    
        - 40    
        - 41    
        - 42    
        - 43    
        - 44    
        - 45    
        - 46    
        - 47    
        - 48    
        - 49    
        - 50    
        - 51    
        - 52    
        - 53    
        - 54    
        - 55    
        - 56    
        - 57    
        - 58    
        - 59    
        - 60    
        - 61    
        - 62    
        - 63    
        - 64    
        - 65    
        - 66    
        - 67    
        - 68    
        - 69    
        - 70    
        - 71    
        - 72    
        - 73    
        - 74    
        - 75    
        - 76    
        - 77    
        - 78    
        - 79    
        - 80    
        - 81    
        - 82    
        - 83    
        - 84    
        - 85    
        - 86    
        - 87    
        - 88    
        - 89    
        - 90    
        - 91    
        - 92    
        - 93    
        - 94    
        - 95    
        - 96    
        - 97    
        - 98    
        - 99    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vesselType:    
      description: 'Enum:''1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other''. Code for vessel type'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/MasterVessel/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 마스터베슬 NGSI-v2 키값 예시  
다음은 키 값으로 JSON-LD 형식의 MasterVessel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12  
}  
```  
</details>  
#### MasterVessel NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 MasterVessel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
  },  
  "imo": {  
    "type": "Number",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Number",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Text",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Number",  
    "value": 2  
  },  
  "vesselClass": {  
    "type": "Text",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Number",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Number",  
    "value": 7  
  },  
  "loa": {  
    "type": "Number",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Number",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Number",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Number",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Date-Time",  
    "value": "2023-06-01"  
  },  
  "toBow": {  
    "type": "Number",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Number",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Number",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Number",  
    "value": 4  
  },  
  "photo": {  
    "type": "Text",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Text",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Text",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Text",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Text",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Number",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Number",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Number",  
    "value": 12  
  }  
}  
```  
</details>  
#### 마스터베셀 NGSI-LD 키값 예시  
다음은 키 값으로 JSON-LD 형식의 MasterVessel 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/refs/heads/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MasterVessel NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 MasterVessel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
  },  
  "imo": {  
    "type": "Property",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Property",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Property",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Property",  
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Property",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Property",  
    "value": 2  
  },  
  "vesselClass": {  
    "type": "Property",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Property",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Property",  
    "value": 7  
  },  
  "loa": {  
    "type": "Property",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Property",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Property",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Property",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "value": "2023-06-01"  
    }  
  },  
  "toBow": {  
    "type": "Property",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Property",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Property",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Property",  
    "value": 4  
  },  
  "photo": {  
    "type": "Property",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Property",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Property",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Property",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Property",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Property",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Property",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Property",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Property",  
    "value": 12  
  }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
각 분야의 표준 식별에 동의하기 위해 보류 중입니다. URN 형성에는 다음 표준이 고려됩니다 - SO 3166-1 - 국가 코드 및 세분화 코드에 대한 국제 표준. - RFC 2141 - URN 구문(https://www.ietf.org/rfc/rfc2141.txt) - RFC 8141 - 유니폼 리소스 이름(URN)(https://tools.ietf.org/html/rfc8141) - IALA MRN 요청(https://www.iana.org/assignments/urn-formal/mrn)  
<MRN> ::= "urn" ":" "mrn" ":" <OID> ":" <OSNID> ":" <OSNS> <OID> ::= (알파벳) 0*32(알파벳 / "-") (알파벳) ; 조직 ID (예. ESHUV) <OSNID> ::= (알파넘) 0*32(알파넘 / "-") (알파넘) ; 조직별 네임스페이스 ID(예: 포트콜) <OSNS> ::= pchar *(pchar / "/") ; 조직별 네임스페이스 문자열(예: 모듈 또는 마이크로서비스 이름). <ID> ::= 해당 네임스페이스의 고유 식별자(예: SQL 데이터베이스에서 엔티티 이름 뒤에 오는 행-id)  
예: urn := "urn:mrn:eshuv:portcalls:portcall:id:343"  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
