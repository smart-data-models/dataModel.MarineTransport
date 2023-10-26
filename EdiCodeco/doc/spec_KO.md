<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: EdiCodeco  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **터미널, 장치장 등에서 지정된 컨테이너가 내륙 운송업체(도로, 철도 또는 바지선)에 의해 인도 또는 픽업되었음을 확인하는 메시지입니다. 이 메시지는 터미널 내부 컨테이너 이동(선박 적재 및 하역 제외)을 보고하고 컨테이너가 물리적으로 이동하지 않은 상태에서 컨테이너의 상태 변경을 보고하는 데에도 사용할 수 있습니다. UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)**를 참조하세요.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `ata[date-time]`: 터미널 도착 또는 출발의 실제 시간입니다. (ISO 8601 UTC 형식). UNTDID - D.95B - 세그먼트 DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)을 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `bookingCode[string]`: 예약 참조. UNTDID - D.95B - 세그먼트 RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)을 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerCarrierIdentification[string]`: 거래에 관련된 당사자를 식별하는 코드. UNTDID - D.95B - 세그먼트 NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerClass[string]`: 컨테이너 클래스(장비와 관련된 작업 표시). 열거형: '대륙, 수출, 수입, 선내 잔류, 시프터, 환적'. UNTDID - D.95B - 세그먼트 EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm) 참조.  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIdentification[string]`: 컨테이너 식별. UNTDID - D.95B - 세그먼트 EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)을 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIsoCode[string]`: 장비의 크기와 유형에 대한 코딩된 설명. 열거형 '다임 코팅 탱크, 에폭시 코팅 탱크, IMO1, IMO2, IMO3, 가압 탱크, 냉장 탱크, 반냉장, 스테인리스 스틸 탱크, 비작업 리퍼 컨테이너 40 피트, 박스 팔레트, 유로 팔레트, 스칸디나비아 팔레트, 트레일러, 비작업 리퍼 컨테이너 20 피트, 교환 가능한 팔레트, 세미 트레일러, 탱크 컨테이너 20 피트...,탱크 컨테이너 30 피트, 탱크 컨테이너 40 피트, 컨테이너 IC 20 피트, 컨테이너 IC 30 피트, 컨테이너 IC 40 피트, 냉장고 탱크 20 피트, 냉장고 탱크 30 피트, 냉장고 탱크 40 피트, 탱크 컨테이너 IC 20 피트, 탱크 컨테이너 IC 30 피트, 탱크 컨테이너 IC 40 피트, 냉장고 탱크 IC 20 피트, 냉장고 탱크 40 피트, 이동식 케이스: L < 6,15m, 이동식 케이스: 6,15m < L < 7,82m, 이동식 케이스: 7,82m < L < 9,15m, 이동식 케이스: 9,15m < L < 10,90m, 이동식 케이스: 10,90m < L < 13,75m, 토트빈, 온도 조절 컨테이너 20 피트, 온도 조절 컨테이너 40 피트'. UNTDID - D.95B - 세그먼트 EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm) 참조.  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerSeal[string]`: 컨테이너에 부착된 맞춤형 씰 또는 다른 씰의 번호입니다. UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)을 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerWeight[number]`: 컨테이너의 무게. UNTDID - D.95B - 세그먼트 MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)를 참조하세요.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `destination[string]`: 컨테이너의 최종 목적지(UN/LOCODE: 국제연합 무역 및 운송 위치 코드). UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) 및 [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationTransportType[string]`: 운송 방법 코드(UN/ECE). UNTDID - D.95B - 세그먼트 TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) 및 [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dischargingPort[string]`: 컨테이너가 하역되는 항구(UN/LOCODE: 국제연합 무역 및 운송 위치 코드). UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) 및 [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `fileName[string]`: EDI 코데코 메시지의 파일 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `functionCode[string]`: 메시지의 기능을 나타내는 코드입니다. Enum='취소, 추가, 삭제, 변경, 교체, 확인, 중복, 상태, 원본, 찾을 수 없음, 응답, 처리되지 않음, 요청, 사전 알림, 알림, 제안, 취소, 재발행 예정, 재발행, 판매자 시작 변경, 제목 섹션만 교체, 항목 상세 및 요약만 교체, 최종 전송, 거래 보류 중, 배송 지시, 예상, 배송 지시 및 예상, 수락 안 됨, 수락함, 제목 섹션에 수정 포함, 수정 없이 수락함, 수락, 세부 사항 섹션 수정 후 수락, 복사, 승인, 제목 섹션 변경, 수정 후 수락, 재전송, 세부 사항 섹션 변경, 출금 취소, 입금 취소, 삭제 요청, 마감/마감 주문, 특정 수단을 통한 확인, 추가 전송, 유보 없이 수락, 유보 후 수락, 잠정, 확정, 수락, 내용 거부, 분쟁 해결, 철회, 승인, 수정 제안, 테스트'. UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm) 참조.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[string]`: 엔티티의 고유 식별자  - `isContainerEmpty[boolean]`: 컨테이너가 가득 찼는지 또는 비어 있는지에 대한 정보. UNTDID - D.95B - 세그먼트 EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)를 참조하세요.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `loadingPort[string]`: 컨테이너가 적재된 항구(UN/LOCODE: 국제연합 무역 및 운송 위치 코드). UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) 및 [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `messageRaw[string]`: EDI 코데코의 원시 메시지  . Model: [https://schema.org/Text](https://schema.org/Text)- `messageVersion[string]`: 메시지 유형의 버전입니다. UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 이 항목의 이름  - `operationType[string]`: 위치의 기능을 식별하는 코드입니다. Enum: '배송 조건 장소, 결제 장소, 물품 수령 장소, 출발지, 배송 장소, 목적지, 적재 장소/항구, 인수 장소, 양륙 장소/항구, 출항 장소, 환적 장소, 물품 위치, 양도 책임 장소, 소유권 이전 장소, 국경 통과 장소, 창고, 공장/공장, 물품 최종 목적지, 판매 조건 장소, 통관 세관, 출고 항구, 입국 항구, 국가, 도시, 원산지 국가, 물품 목적지 국가, 철도역, 공급원 국가, 건물, 과세 구간 시작, 반출 거점항, 선적 거점항, 수출/배송 국가, 최종 목적지 국가, 최종 위탁 국가, 최초 목적지 국가, 생산 국가, 거래 국가, 입국 세관, 출국 세관, 세관 심사 장소, 서류 인증 장소, 도착(환승) 세관, 배송 지역, 도착지 지역, 생산지 지역, 경유지 국가, 경유지 세관, 유효하지 않은 운송 보증 국가, 도착지(경유지) 국가, 요금 및 운임 지급처, 제조 부서, 요금 및 운임 지급처, 청구 구간 종료, 지급 장소, 전철 적재 또는 하역, 도착지, 다음 기항지, 운송 중 항구, 최초 선택 양하 장소, 고속 철도역, 혼합 화물 철도역, 두 번째 선택 양하 장소, 다음 비양하 기항지, 세 번째 선택적 양하 장소, 재통합 지점, 네 번째 선택적 양하 장소, 선하증권 발행 사무소, 이곳을 제외한 환적, 이곳으로 제한된 환적, 최초 선적항, 최초 기항지 - 비양하, 최초 기항지 - 양하, 최초 입국 장소/항, 발송 장소, 다섯 번째 선택적 양하 장소, 운송 전 항구, 인도 장소(운송 중), 운송 계약 인수 장소, 운송 계약 목적지, 유효한 운송 보증 국가, 운송 최초 도착지/항구, 수령지, 등록지, 특별 대우가 발생했거나 발생해야 하는 장소/위치, 서류 발급지, 경로, 추가 비용 적용지, 서류 보관지, 선택적 배출지, 빈 장비 발송지, 빈 장비 반송지, 창고 입고지/항구, 최초 판매 국가, 구매 국가, 양수 장소, 해체 장소, 소비 장소, 원산지 지역, 통합 장소, 요금 결합 지점, 배송 지연 연장 결정 장소, 재충전 장소/위치, 발송 세관, 발송 국가, 수출 세관, 수출 자유 지역, 수출/발송 지역, 출발 세관, 환적 보증 세관, 환적 국가, 판매 국가, 도착 세관, 화차 선적 철도역, 사이딩, 운송의 최종 기항지/항구, 이전 세관 절차 국가, 이전 세관 신고 등록 세관, 참가자 발송인 위치, 임금 협상 지역, 운송의 최종 목적지, 공장비 적재 장소, 공장비 배출 장소, 배송 지역, 석유 창고, 입국 장소(세관), 살아있는 동물 관리 장소, 재제빙 장소, 중량 측정 장소, 마샬링 야드, 쇼핑 스테이션, 적재 부두, 항만 연결, 만기 장소, 협상 장소, 클레임 지불 장소, 서류 크레딧 가능 장소, 적재 셀, 운송용, 선내 적재/배달/출항지/출발지, 전용 박스, 다음 양하항, 기항지, 고용 장소/위치, 고용 장소/위치, 타 항공사 터미널, 부가가치세 관할 국가, 연락처 위치, 추가 내항지, 외국 기항지, 정비 장소 상호 정의'로 표기합니다. UNTDID - D.95B - Segment TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm) 참조.  . Model: [https://schema.org/Text](https://schema.org/Text)- `originTransportType[string]`: 운송 방법 코드(UN/ECE). UNTDID - D.95B - 세그먼트 TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) 및 [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `receiverIdentification[string]`: 교환 수취인 신원 확인. UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B) 참조  . Model: [https://schema.org/Text](https://schema.org/Text)- `release[string]`: 현재 버전 번호 내의 릴리스 번호. UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `senderIdentification[string]`: 교환 발신자 식별. UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B) 참조  . Model: [https://schema.org/Text](https://schema.org/Text)- `sentAt[date-time]`: 메시지가 전송된 날짜와 시간은 ISO 8601 UTC 형식으로 표시됩니다. UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `travelReference[string]`: 운송 참조 번호. UNTDID - D.95B - 세그먼트 TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)을 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `truckLicenseCode[string]`: 트럭의 번호판. UNTDID - D.95B - 세그먼트 TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 엔티티 유형. EdiCodeco여야 합니다.  - `vesselCallSign[string]`: 해상 호출 부호는 선박에 고유 식별자로 할당된 호출 부호입니다. UNTDID - D.95B - 세그먼트 TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselCarrier[string]`: 선박 운송인 식별 (지정된 지점 간 물품 운송을 수행하거나 주선하는 당사자의 식별). UNTDID - D.95B - 세그먼트 TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)을 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselImo[number]`: 국제해사기구 번호(글로벌 영구 UID). UNTDID - D.95B - 세그먼트 TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)를 참조하세요.  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselMmsi[number]`: 해양 모바일 서비스 식별 번호(해당 개체의 현재 플래그 상태에 의해 임시로 할당된 UID). UNTDID - D.95B - 세그먼트 TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)를 참조하세요.  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselName[string]`: 선박 이름. UNTDID - D.95B - 세그먼트 TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselVoyage[string]`: 선박 항해의 참조 번호. UNTDID - D.95B - 세그먼트 RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)를 참조하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `containerIdentification`  - `id`  - `type`  - `vesselImo`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EdiCodeco:    
  description: 'A message by which a terminal, depot, etc. confirms that the containers specified have been delivered or picked up by the inland carrier (road, rail or barge). This message can also be used to report internal terminal container movements (excluding loading and discharging the vessel) and to report the change in status of container(s) without those containers having physically been moved. See [UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)'    
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
    ata:    
      description: 'Actual time of arrival or departure to/from Terminal. (ISO 8601 UTC format). See [UNTDID - D.95B - Segment DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bookingCode:    
      description: 'Booking Reference. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerCarrierIdentification:    
      description: 'Code identifying a party involved in a transaction. See [UNTDID - D.95B - Segment NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerClass:    
      description: 'Container class (indication of the action related to the equipment). Enum: ''Continental, Export, Import,Remain on board,Shifter,Transhipment''. See [UNTDID - D.95B - Segment EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm)'    
      enum:    
        - Continental    
        - Export    
        - Import    
        - Remain on board    
        - Shifter    
        - Transhipment    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerIdentification:    
      description: 'Containter identification. See [UNTDID - D.95B - Segment EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerIsoCode:    
      description: 'Coded description of the size and type of equipment. Enum ''Dime coated tank,Epoxy coated tank,IMO1,IMO2,IMO3,Pressurized tank,Refrigerated tank,Semi-refrigerated,Stainless steel tank,Nonworking reefer container 40 ft,Box pallet,Europallet,Scandinavian pallet,Trailer,Nonworking reefer container 20 ft,Exchangeable pallet,Semi-trailer,Tank container 20 ft.,Tank container 30 ft.,Tank container 40 ft.,Container IC 20 ft.,Container IC 30 ft.,Container IC 40 ft.,Refrigerator tank 20 ft.,Refrigerator tank 30 ft.,Refrigerator tank 40 ft.,Tank container IC 20 ft.,Tank container IC 30 ft.,Tank container IC 40 ft.,Refrigerator tank IC 20 ft.,Refrigerator tank IC 40 ft.,Movable case: L < 6,15m,Movable case: 6,15m < L < 7,82m,Movable case: 7,82m < L < 9,15m,Movable case: 9,15m < L < 10,90m,Movable case: 10,90m < L < 13,75m,Totebin,Temperature controlled container 20 ft,Temperature controlled container 40 ft''. See [UNTDID - D.95B - Segment EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)'    
      enum:    
        - Dime coated tank    
        - Epoxy coated tank    
        - IMO1    
        - IMO2    
        - IMO3    
        - Pressurized tank    
        - Refrigerated tank    
        - Semi-refrigerated    
        - Stainless steel tank    
        - Nonworking reefer container 40 ft    
        - Box pallet    
        - Europallet    
        - Scandinavian pallet    
        - Trailer    
        - Nonworking reefer container 20 ft    
        - Exchangeable pallet    
        - Semi-trailer    
        - Tank container 20 ft.    
        - Tank container 30 ft.    
        - Tank container 40 ft.    
        - Container IC 20 ft.    
        - Container IC 30 ft.    
        - Container IC 40 ft.    
        - Refrigerator tank 20 ft.    
        - Refrigerator tank 30 ft.    
        - Refrigerator tank 40 ft.    
        - Tank container IC 20 ft.    
        - Tank container IC 30 ft.    
        - Tank container IC 40 ft.    
        - Refrigerator tank IC 20 ft.    
        - Refrigerator tank IC 40 ft.    
        - 'Movable case: L < 6,15m'    
        - 'Movable case: 6,15m < L < 7,82m'    
        - 'Movable case: 7,82m < L < 9,15m'    
        - 'Movable case: 9,15m < L < 10,90m'    
        - 'Movable case: 10,90m < L < 13,75m'    
        - Totebin    
        - Temperature controlled container 20 ft    
        - Temperature controlled container 40 ft    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerSeal:    
      description: 'The number of a custom seal or another seal affixed to the containers. See [UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerWeight:    
      description: 'Weight of the container. See [UNTDID - D.95B - Segment MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: ' KGM'    
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
    destination:    
      description: 'Final destination of the container (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationTransportType:    
      description: 'Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dischargingPort:    
      description: 'Port where the container is discharged (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fileName:    
      description: File name of EDI Codeco message    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    functionCode:    
      description: 'Code indicating the function of the message. Enum=''Cancellation, Addition, Deletion, Change, Replace, Confirmation, Duplicate, Status, Original, Not found, Response, Not processed, Request, Advance notification, Reminder, Proposal, Cancel, to be reissued, Reissue, Seller initiated change, Replace heading section only, Replace item detail and summary only, Final transmission, Transaction on hold, Delivery instruction, Forecast, Delivery instruction and forecast, Not accepted, Accepted, with amendment in heading section, Accepted without amendment, Accepted, with amendment in detail section, Copy, Approval, Change in heading section, Accepted with amendment, Retransmission, Change in detail section, Reversal of a debit, Reversal of a credit, Reversal for cancellation, Request for deletion, Finishing/closing order, Confirmation via specific means, Additional transmission, Accepted without reserves, Accepted with reserves, Provisional, Definitive, Accepted, contents rejected, Settled dispute, Withdraw, Authorisation, Proposed amendment, Test''. See [UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)'    
      enum:    
        - Cancellation    
        - Addition    
        - Deletion    
        - Change    
        - Replace    
        - Confirmation    
        - Duplicate    
        - Status    
        - Original    
        - Not found    
        - Response    
        - Not processed    
        - Request    
        - Advance notification    
        - Reminder    
        - Proposal    
        - 'Cancel, to be reissued'    
        - Reissue    
        - Seller initiated change    
        - Replace heading section only    
        - Replace item detail and summary only    
        - Final transmission    
        - Transaction on hold    
        - Delivery instruction    
        - Forecast    
        - Delivery instruction and forecast    
        - Not accepted    
        - 'Accepted, with amendment in heading section'    
        - Accepted without amendment    
        - 'Accepted, with amendment in detail section'    
        - Copy    
        - Approval    
        - Change in heading section    
        - Accepted with amendment    
        - Retransmission    
        - Change in detail section    
        - Reversal of a debit    
        - Reversal of a credit    
        - Reversal for cancellation    
        - Request for deletion    
        - Finishing/closing order    
        - Confirmation via specific means    
        - Additional transmission    
        - Accepted without reserves    
        - Accepted with reserves    
        - Provisional    
        - Definitive    
        - 'Accepted, contents rejected'    
        - Settled dispute    
        - Withdraw    
        - Authorisation    
        - Proposed amendment    
        - Test    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      description: Unique identifier of the entity    
      type: string    
      x-ngsi:    
        type: Property    
    isContainerEmpty:    
      description: 'Information about if the container is full or empty. See [UNTDID - D.95B - Segment EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    loadingPort:    
      description: 'Port where the container is loaded (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    messageRaw:    
      description: Raw message of the EDI Codeco    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    messageVersion:    
      description: "Version of the message type. See [UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'Code identifying the function of a location. Enum: ''Place of terms of delivery, Payment place, Goods receipt place, Place of departure, Place of delivery, Place of destination, Place/port of loading, Place of acceptance, Place/port of discharge, Port of discharge, Place of transhipment, Location of goods, Place of transfer responsibility, Place of transfer of ownership, Border crossing place, Warehouse, Factory/plant, Place of ultimate destination of goods, Terms of sale place, Customs office of clearance, Port of release, Port of entry, Country, City, Country of origin, Country of destination of goods, Railway station, Country of source, Building, Beginning of chargeable section, Baseport of discharge, Baseport of loading, Country of exportation/despatch, Country of ultimate destination, Country of last consignment, Country of first destination, Country of production, Country of trading, Customs office of entry, Customs office of exit, Place of Customs examination, Place of authentication of document, Customs office of destination (transit), Region of despatch, Region of destination, Region of production, Country of transit, Customs office of transit, Country of invalid transit guarantee, Country of destination (transit), Charge and freight due from, Manufacturing department, Charges and freight payable to, End of chargeable section, Place of payment, Full track loading or unloading, Place of arrival, Next port of call, On-carriage port, First optional place of discharge, Express railway station, Mixed cargo railway station, Second optional place of discharge, Next non-discharge port of call, Third optional place of discharge, Reconsolidation point, Fourth optional place of discharge, Bill of lading release office, Transhipment excluding this place, Transhipment limited to this place, Original port of loading, First port of call - non-discharging, First port of call - discharging, Place/port of first entry, Place of despatch, Fifth optional place of discharge, Pre-carriage port, Place of delivery (by on carriage), Transport contract place of acceptance, Transport contract place of destination, Country of valid transit guarantee, Place/port of conveyance initial arrival, Place of receipt, Place of registration, Place/location where special treatments have happened or must happen, Place of document issue, Routing, Station of application of additional costs, Place of lodgement of documents, Optional place of discharge, Place of empty equipment despatch, Place of empty equipment return, Place/port of warehouse entry, Country of first sale, Country of purchase, Place of transfer, Place of deconsolidation, Place of consumption, Region of origin, Place of consolidation, Rate combination point, Place of prolongation decision of delivery delay, Recharging place/location, Customs office of despatch, Country of despatch, Customs office of export, Free zone of export, Region of export/despatch, Customs office of departure, Customs office of transit guarantee, Country of transhipment, Country of sale, Customs office of destination, Wagon-load railway station, Siding, Last place/port of call of conveyance, Country of previous Customs procedure, Customs office of registration of previous Customs declaration, Participant sender location, Wage negotiation district, Place of ultimate destination of conveyance, Place of loading of empty equipment, Place of discharge of empty equipment, Region of delivery, Petroleum warehouse, Place of entry (Customs), Living animals care place, Re-icing place, Weighting place, Marshalling yard, Shopping station, Loading dock, Port connection, Place of expiry, Place of negotiation, Claims payable place, Documentary credit available in, Stowage cell, For transportation to, Loading on board/despatch/taking in charge at/from, Private box, Next port of discharge, Port of call, Place/location of on-hire, Place/location of off-hire, Other carriers terminal, Country of Value Added Tax (VAT) jurisdiction, Contact location, Additional internal destination, Foreign port of call, Maintenance location    
        Mutually defined''. See [UNTDID - D.95B - Segment TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)'    
      enum:    
        - Place of terms of delivery    
        - Payment place    
        - Goods receipt place    
        - Place of departure    
        - Place of delivery    
        - Place of destination    
        - Place/port of loading    
        - Place of acceptance    
        - Place/port of discharge    
        - Port of discharge    
        - Place of transhipment    
        - Location of goods    
        - Place of transfer responsibility    
        - Place of transfer of ownership    
        - Border crossing place    
        - Warehouse    
        - Factory/plant    
        - Place of ultimate destination of goods    
        - Terms of sale place    
        - Customs office of clearance    
        - Port of release    
        - Port of entry    
        - Country    
        - City    
        - Country of origin    
        - Country of destination of goods    
        - Railway station    
        - Country of source    
        - Building    
        - Beginning of chargeable section    
        - Baseport of discharge    
        - Baseport of loading    
        - Country of exportation/despatch    
        - Country of ultimate destination    
        - Country of last consignment    
        - Country of first destination    
        - Country of production    
        - Country of trading    
        - Customs office of entry    
        - Customs office of exit    
        - Place of Customs examination    
        - Place of authentication of document    
        - Customs office of destination (transit)    
        - Region of despatch    
        - Region of destination    
        - Region of production    
        - Country of transit    
        - Customs office of transit    
        - Country of invalid transit guarantee    
        - Country of destination (transit)    
        - Charge and freight due from    
        - Manufacturing department    
        - Charges and freight payable to    
        - End of chargeable section    
        - Place of payment    
        - Full track loading or unloading    
        - Place of arrival    
        - Next port of call    
        - On-carriage port    
        - First optional place of discharge    
        - Express railway station    
        - Mixed cargo railway station    
        - Second optional place of discharge    
        - Next non-discharge port of call    
        - Third optional place of discharge    
        - Reconsolidation point    
        - Fourth optional place of discharge    
        - Bill of lading release office    
        - Transhipment excluding this place    
        - Transhipment limited to this place    
        - Original port of loading    
        - First port of call - non-discharging    
        - First port of call - discharging    
        - Place/port of first entry    
        - Place of despatch    
        - Fifth optional place of discharge    
        - Pre-carriage port    
        - Place of delivery (by on carriage)    
        - Transport contract place of acceptance    
        - Transport contract place of destination    
        - Country of valid transit guarantee    
        - Place/port of conveyance initial arrival    
        - Place of receipt    
        - Place of registration    
        - Place/location where special treatments have happened or must happen    
        - Place of document issue    
        - Routing    
        - Station of application of additional costs    
        - Place of lodgement of documents    
        - Optional place of discharge    
        - Place of empty equipment despatch    
        - Place of empty equipment return    
        - Place/port of warehouse entry    
        - Country of first sale    
        - Country of purchase    
        - Place of transfer    
        - Place of deconsolidation    
        - Place of consumption    
        - Region of origin    
        - Place of consolidation    
        - Rate combination point    
        - Place of prolongation decision of delivery delay    
        - Recharging place/location    
        - Customs office of despatch    
        - Country of despatch    
        - Customs office of export    
        - Free zone of export    
        - Region of export/despatch    
        - Customs office of departure    
        - Customs office of transit guarantee    
        - Country of transhipment    
        - Country of sale    
        - Customs office of destination    
        - Wagon-load railway station    
        - Siding    
        - Last place/port of call of conveyance    
        - Country of previous Customs procedure    
        - Customs office of registration of previous Customs declaration    
        - Participant sender location    
        - Wage negotiation district    
        - Place of ultimate destination of conveyance    
        - Place of loading of empty equipment    
        - Place of discharge of empty equipment    
        - Region of delivery    
        - Petroleum warehouse    
        - Place of entry (Customs)    
        - Living animals care place    
        - Re-icing place    
        - Weighting place    
        - Marshalling yard    
        - Shopping station    
        - Loading dock    
        - Port connection    
        - Place of expiry    
        - Place of negotiation    
        - Claims payable place    
        - Documentary credit available in    
        - Stowage cell    
        - For transportation to    
        - Loading on board/despatch/taking in charge at/from    
        - Private box    
        - Next port of discharge    
        - Port of call    
        - Place/location of on-hire    
        - Place/location of off-hire    
        - Other carriers terminal    
        - Country of Value Added Tax (VAT) jurisdiction    
        - Contact location    
        - Additional internal destination    
        - Foreign port of call    
        - Maintenance location    
        - Mutually defined    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originTransportType:    
      description: 'Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    receiverIdentification:    
      description: 'Interchange Recipient Identification. See [UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    release:    
      description: "Release number within current version number. See [UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)"    
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
    senderIdentification:    
      description: 'Interchange Sender Identification. See [UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    sentAt:    
      description: 'Date and time of message has been sent represented by an ISO 8601 UTC format. See [UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    travelReference:    
      description: 'Conveyance reference number. See [UNTDID - D.95B - Segment TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    truckLicenseCode:    
      description: 'License Plate of the Truck. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be EdiCodeco    
      enum:    
        - EdiCodeco    
      type: string    
      x-ngsi:    
        type: Property    
    vesselCallSign:    
      description: 'Maritime call signs are call signs assigned as unique identifiers to vessels. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselCarrier:    
      description: 'Vessel carrier Identification (identification of party undertaking or arranging transport of goods between named points). See [UNTDID - D.95B - Segment TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselImo:    
      description: 'International Maritime Organization Number (a global forever UID). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vesselMmsi:    
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vesselName:    
      description: 'Vessel Name. See [UNTDID - D.95B - Segment TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselVoyage:    
      description: 'Reference number of vessel voyage. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - vesselImo    
    - containerIdentification    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.MarineTransport/EdiCodeco/schema.json    
  x-model-tags: i4trust    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### EdiCodeco NGSI-v2 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 EdiCodeco의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": "file name",  
    "sentAt": "2023-08-11T14:50:00Z",  
    "travelReference": "110823110823CCHRIB",  
    "ata": "2023-08-11T14:47:00Z",  
    "bookingCode": "FUE110823",  
    "containerCarrierIdentification": "ALU",  
    "containerClass": "Export",  
    "containerIdentification": "TESI1120274",  
    "containerIsoCode": "Refrigerated tank",  
    "containerSeal": "28103",  
    "containerWeight": 27000,  
    "destinationTransportType": "Vessel",  
    "dischargingPort": "ESFUE",  
    "functionCode": "Deletion",  
    "isContainerEmpty": false,  
    "loadingPort": "ESHUV",  
    "operationType": "Port of entry",  
    "originTransportType": "Truck",  
    "messageRaw": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'",  
    "receiverIdentification": "PA",  
    "release": "95B",  
    "senderIdentification": "ESHUV",  
    "truckLicenseCode": "993NGR",  
    "messageVersion": "D",  
    "vesselCarrier": "ALQ",  
    "vesselImo": 1111111,  
    "vesselName": "Name",  
    "vesselVoyage": "110823110823CCHRIB"  
}  
```  
</details>  
#### EdiCodeco NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 에디코코의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": {  
        "type": "Text",  
        "value": "file name"  
    },  
    "sentAt": {  
        "type": "DateTime",  
        "value": "2023-08-11T14:50:00Z"  
    },  
    "travelReference": {  
        "type": "Text",  
        "value": "110823110823CCHRIB"  
    },  
    "ata": {  
        "type": "DateTime",  
        "value": "2023-08-11T14:47:00Z"  
    },  
    "bookingCode": {  
        "type": "Text",  
        "value": "FUE110823"  
    },  
    "containerCarrierIdentification": {  
        "type": "Text",  
        "value": "ALU"  
    },  
    "containerClass": {  
        "type": "Text",  
        "value": "Export"  
    },  
    "containerIdentification": {  
        "type": "Text",  
        "value": "TESI1120274"  
    },  
    "containerIsoCode": {  
        "type": "Text",  
        "value": "Refrigerated tank"  
    },  
    "containerSeal": {  
        "type": "Text",  
        "value": "28103"  
    },  
    "containerWeight": {  
        "type": "Number",  
        "value": 27000  
    },  
    "destinationTransportType": {  
        "type": "Text",  
        "value": "Vessel"  
    },  
    "dischargingPort": {  
        "type": "Text",  
        "value": "ESFUE"  
    },  
    "functionCode": {  
        "type": "Text",  
        "value": "Deletion"  
    },  
    "isContainerEmpty": {  
        "type": "Boolean",  
        "value": false  
    },  
    "loadingPort": {  
        "type": "Text",  
        "value": "ESHUV"  
    },  
    "operationType": {  
        "type": "Text",  
        "value": "Port of entry"  
    },  
    "originTransportType": {  
        "type": "Text",  
        "value": "Truck"  
    },  
    "messageRaw": {  
        "type": "Text",  
        "value": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'"  
    },  
    "receiverIdentification": {  
        "type": "Text",  
        "value": "PA"  
    },  
    "release": {  
        "type": "Text",  
        "value": "95B"  
    },  
    "senderIdentification": {  
        "type": "Text",  
        "value": "ESHUV"  
    },  
    "truckLicenseCode": {  
        "type": "Text",  
        "value": "993NGR"  
    },  
    "messageVersion": {  
        "type": "Text",  
        "value": "D"  
    },  
    "vesselCarrier": {  
        "type": "Text",  
        "value": "ALQ"  
    },  
    "vesselImo": {  
        "type": "Number",  
        "value": 1111111  
    },  
    "vesselName": {  
        "type": "Text",  
        "value": "Name"  
    },  
    "vesselVoyage": {  
        "type": "Text",  
        "value": "110823110823CCHRIB"  
    }  
}  
```  
</details>  
#### EdiCodeco NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 EdiCodeco의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": "file name",  
    "sentAt": "2023-08-11T14:50:00Z",  
    "travelReference": "110823110823CCHRIB",  
    "ata": "2023-08-11T14:47:00Z",  
    "bookingCode": "FUE110823",  
    "containerCarrierIdentification": "ALU",  
    "containerClass": "Export",  
    "containerIdentification": "TESI1120274",  
    "containerIsoCode": "Refrigerated tank",  
    "containerSeal": "28103",  
    "containerWeight": 27000,  
    "destinationTransportType": "Vessel",  
    "dischargingPort": "ESFUE",  
    "functionCode": "Deletion",  
    "isContainerEmpty": false,  
    "loadingPort": "ESHUV",  
    "operationType": "Port of entry",  
    "originTransportType": "Truck",  
    "messageRaw": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'",  
    "receiverIdentification": "PA",  
    "release": "95B",  
    "senderIdentification": "ESHUV",  
    "truckLicenseCode": "993NGR",  
    "messageVersion": "D",  
    "vesselCarrier": "ALQ",  
    "vesselImo": 1111111,  
    "vesselName": "CHRISTIAN",  
    "vesselVoyage": "110823110823CCHRIB",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EdiCodeco NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 에디코코의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": {  
        "type": "Property",  
        "value": "file name"  
    },  
    "sentAt": {  
        "type": "Property",  
        "value": {  
            "@value": "2023-08-11T14:50:00Z",  
            "@type": "DateTime"  
        }  
    },  
    "travelReference": {  
        "type": "Property",  
        "value": "110823110823CCHRIB"  
    },  
    "ata": {  
        "type": "Property",  
        "value": {  
            "@value": "2023-08-11T14:47:00Z",  
            "@type": "DateTime"  
        }  
    },  
    "bookingCode": {  
        "type": "Property",  
        "value": "FUE110823"  
    },  
    "containerCarrierIdentification": {  
        "type": "Property",  
        "value": "ALU"  
    },  
    "containerClass": {  
        "type": "Property",  
        "value": "Export"  
    },  
    "containerIdentification": {  
        "type": "Property",  
        "value": "TESI1120274"  
    },  
    "containerIsoCode": {  
        "type": "Property",  
        "value": "Refrigerated tank"  
    },  
    "containerSeal": {  
        "type": "Property",  
        "value": "28103"  
    },  
    "containerWeight": {  
        "type": "Property",  
        "value": 27000  
    },  
    "destinationTransportType": {  
        "type": "Property",  
        "value": "Vessel"  
    },  
    "dischargingPort": {  
        "type": "Property",  
        "value": "ESFUE"  
    },  
    "functionCode": {  
        "type": "Property",  
        "value": "Deletion"  
    },  
    "isContainerEmpty": {  
        "type": "Property",  
        "value": false  
    },  
    "loadingPort": {  
        "type": "Property",  
        "value": "ESHUV"  
    },  
    "operationType": {  
        "type": "Property",  
        "value": "Port of entry"  
    },  
    "originTransportType": {  
        "type": "Property",  
        "value": "Truck"  
    },  
    "messageRaw": {  
        "type": "Property",  
        "value": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'"  
    },  
    "receiverIdentification": {  
        "type": "Property",  
        "value": "PA"  
    },  
    "release": {  
        "type": "Property",  
        "value": "95B"  
    },  
    "senderIdentification": {  
        "type": "Property",  
        "value": "ESHUV"  
    },  
    "truckLicenseCode": {  
        "type": "Property",  
        "value": "993NGR"  
    },  
    "messageVersion": {  
        "type": "Property",  
        "value": "D"  
    },  
    "vesselCarrier": {  
        "type": "Property",  
        "value": "ALQ"  
    },  
    "vesselImo": {  
        "type": "Property",  
        "value": 1111111  
    },  
    "vesselName": {  
        "type": "Property",  
        "value": "Name"  
    },  
    "vesselVoyage": {  
        "type": "Property",  
        "value": "110823110823CCHRIB"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
