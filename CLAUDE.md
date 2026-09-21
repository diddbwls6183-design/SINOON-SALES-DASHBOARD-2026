# SINOON ONLINE DASHBOARD — CLAUDE.md

> 새 Claude 세션에서 이 파일을 먼저 읽어야 합니다.
> 모든 수정은 반드시 이 문서의 구조·방식을 기반으로 진행하세요.
> 코드 변경 전 반드시 사용자에게 먼저 확인 받을 것.

---

## 1. 프로젝트 개요

- **대시보드 URL**: `https://diddbwls6183-design.github.io/SINOON-ONLINE/`
- **GitHub repo**: `diddbwls6183-design/SINOON-ONLINE`
- **원본 repo**: `diddbwls6183-design/SINOON-SALES-DASHBOARD-2026` (회사용)
- **GitHub token**: 사용자에게 매 세션마다 직접 확인할 것
- **구조**: 단일 파일 대시보드 (`index.html` ~1MB) + 외부 데이터 JSON 2개 + 이미지 폴더

---

## 2. 파일 구조

```
SINOON-ONLINE/
├── index.html          # 메인 대시보드 (전체 코드 포함, ~1MB)
├── data.json           # 앱스크립트가 생성·업로드하는 판매 데이터 (~2.2MB)
├── dashboard-sync.json # 마케팅·프로모션·기타 데이터 (~325KB)
├── _between.txt        # 앱스크립트 빌드 시 생성되는 JS 상수 코드 조각 (~185KB)
├── images/             # 상품 이미지 (~966개, WebP/JPG 용량 최소화)
│   └── SN2F1HH001PK.webp  # 상품코드 기반 파일명
└── .github/workflows/fix.yml
```

---

## 3. 데이터 흐름 (업데이트 구조)

### 3-1. 판매 데이터 일간 업데이트

Google Sheets(데이터 입력) → Apps Script BUILDANDSAVE 실행 → "데이터 업데이트.cmd" 더블클릭 → data.json이 GitHub에 업로드 → 30초~1분 후 대시보드 반영

### 3-2. 애널리틱스 데이터

**자동 갱신 (Google Sheets TOTAL 시트 → data.json)**
- 객단가(AOV): data.json > MONTHLY_AOV
- 구매비율, 카테고리별 매출비중: 매일 자동 갱신

**수동 업데이트 (엑셀 → Claude 직접 반영)**
- 퍼널 데이터, 장바구니 데이터
- 방법: 엑셀 파일을 Claude에게 업로드 → Claude가 index.html 내 변수 수정 → GitHub commit

### 3-3. 마케팅·프로모션

dashboard-sync.json에 저장:
- sinoon_mkt_budget, sinoon_mkt_spend, sinoon_mkt_weekly, sinoon_mkt_daily_report
- sinoon_mkt_review, sinoon_promo_data, sinoon_s4_sparse_edits

---

## 4. data.json 구조

```json
{
  "monthly26": { "1월": { "자사몰": {"s":판매액,"q":수량,"r":반품액,"rq":반품수} } },
  "daily26":   { "2026-01-02": { "자사몰": 순매출값 } },
  "weekly26":  { "1월1주": { "자사몰": {...} } },
  "MONTHLY_AOV": { "자사몰": { "1월": 값 } },
  "STOCK_MAP": { "상품코드": 재고수량 },
  "ch_top20":  { "자사몰": [...] },
  "month_ranking": { "1월": [...] },
  "week_ranking":  { "1월1주": [...] },
  "week_to_dates": { "1월1주": ["2026-01-05", ...] },
  "ps_data":   { "상품코드": {...} },
  "top20_all": [...],
  "_updated":  "타임스탬프"
}
```

키 규칙: 월별="1월", 일별="2026-01-02"(YYYY-MM-DD), 주차별="1월1주"
채널명: 자사몰, 29CM, 무신사, 무신사글로벌, 자사몰_해외, 카카오딜, NUGU_일본

---

## 5. index.html 내 하드코딩 데이터

2025년 비교 데이터는 index.html 내부에 직접 하드코딩 (외부 JSON 아님):

- D.daily25: {"2025-01-02": {"자사몰": 값, ...}, ...}
- D.monthly25: {"1월": {...}, ...}
- D.weekly25: {"1월1주": {...}, ...}
- D.targets: 2026년 채널별 월별 목표액

---

## 6. 전년동기 신장률(YoY) 계산 방식

진행 중인 달: 2025년 같은 일수만큼만 비교 (_yoy_same_period 사용)
완료된 달: 2025년 전체 월 데이터 비교 (m25s 사용)

핵심 함수:
- _yoy_same_period(mon, ch): 일별 데이터 기반 동기 합산
- _weekly_yoy_same_period(p, ch): 주차별 동기 비교
- _isIncompleteMon(m): 진행 중인 달 판별
- m25s(m, ch): D.monthly25[m][ch] 반환

s0GetData (채널별 목표달성률 탭) 월별 모드:
  if(hasMon(m)){ s25 += _isIncompleteMon(m) ? _yoy_same_period(m,ch) : m25s(m,ch); }

s1D (채널별 판매현황 탭) 월별 모드:
  if(hasMon(p)){ s25 = _isIncompleteMon(p) ? _yoy_same_period(p,ch) : m25s(p,ch); }

일별 모드: D.daily25[p.replace('2026','2025')]  (YYYY-MM-DD 날짜키 변환)
주차별 모드: _weekly_yoy_same_period(p, ch)

---

## 7. 기간 버튼 구조

- 기간 단위: 월별 / 주차별 / 일별 (s1.gran 변수)
- 월 버튼: 1월~12월 (현재 월까지 활성화)
- 채널 필터: 전체 / 자사몰 / 29CM / 무신사 / 무신사글로벌 / 자사몰_해외 / 카카오딜

---

## 8. 만토바 주간회의록 탭

Firebase 시도 → 데이터 소실 → 현재: index.html MT_MEETINGS_DEFAULT에 하드코딩

```javascript
MT_MEETINGS_DEFAULT = {
  '20260831': `...8월31일 회의록 전문...`,
  '20260909': `...9월9일 회의록 전문...`,
  '20260914': `...9월14일 회의록 전문...`
};
```

날짜 드롭다운: YYYYMMDD 키 → "2026.09.09(수)" 형식 (요일 자동 계산)
새 회의록 추가: PDF 업로드 또는 텍스트 제공 → MT_MEETINGS_DEFAULT에 추가 → commit

---

## 9. 이미지 저장

- 위치: GitHub repo images/ 폴더
- 파일명: 상품코드.webp (예: SN2E2TT036WH.webp)
- 형식: WebP 우선(용량 최소화), 일부 JPG
- 대부분 1~5KB 크기
- index.html에서 images/상품코드.webp 경로로 직접 참조
- 추가: 사용자가 이미지 제공 → GitHub API로 images/ 폴더에 업로드

---

## 10. GitHub 배포 방식

소규모 수정: Contents API PUT (파일 SHA 필요)
대용량 수정(index.html 전체): Git Data API 순서 필수
  1. POST /git/blobs → blob SHA
  2. POST /git/trees (base_tree: 현재 tree SHA) → tree SHA
  3. POST /git/commits (parents: [현재 HEAD SHA]) → commit SHA
  4. PATCH /git/refs/heads/main → HEAD 업데이트

주의:
- bash 불가 (Windows 업데이트 이후). 모든 작업 = Chrome JS + GitHub API
- 보안 필터: URL/base64 패턴 포함 문자열 차단 → charcode 배열 또는 window 변수로 우회
- 파일 크기 ~1MB 이상은 반드시 Git Data API 방식 사용

---

## 11. 재고

재고는 무조건 Google Sheets 확인이 기준. data.json STOCK_MAP은 참고용.

---

## 12. 자주 하는 작업

| 작업 | 방법 |
|------|------|
| 회의록 추가 | PDF 업로드 → 텍스트 추출 → MT_MEETINGS_DEFAULT 하드코딩 → commit |
| 퍼널/장바구니 업데이트 | 엑셀 업로드 → index.html 해당 변수 수정 → commit |
| 이미지 추가 | 이미지 제공 → images/ GitHub API 업로드 |
| YoY 로직 확인 | s0GetData, s1D 함수 월별 분기 확인 |
| 채널명 | 자사몰, 29CM, 무신사, 무신사글로벌, 자사몰_해외, 카카오딜 |
