from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl, field_validator
from enum import Enum
from datetime import datetime


class ErrorResponse(BaseModel):
    error: str


# Площадки
class PlatformType(Enum):
    INVALID = "PLATFORM_TYPE_INVALID"  # тип площадки не определён
    SITE = "PLATFORM_TYPE_SITE"  # сайт
    APP = "PLATFORM_TYPE_APP"  # приложение
    SYSTEM = "PLATFORM_TYPE_SYSTEM"  # информационная система


class OrderBy(Enum):
    ASC = "ASC"
    DESC = "DESC"


class ApiResponse(BaseModel):
    success: bool
    data: dict
    message: str


class PlatformData(BaseModel):
    appName: str
    externalPlatformId: str
    platformType: PlatformType
    url: str
    comment: str

    class Config:
        use_enum_values = True


class UpdatedAt(BaseModel):
    updatedAt: Optional[datetime] = None


class PlatformCursor(BaseModel):
    externalId: str
    updatedAt: Optional[UpdatedAt] = None


class PlatformCreator(BaseModel):
    email: str
    id: str
    name: str


class PlatformEditor(BaseModel):
    email: str
    id: str
    name: str


class PlatformInfo(BaseModel):
    appName: str
    createdAt: str
    createdBy: Optional[PlatformCreator]
    editedAt: Optional[str]
    editedBy: Optional[PlatformEditor]
    externalId: str
    platformId: str
    platformType: str
    url: str
    updatedAt: str
    comment: Optional[str] = None


class PlatformResponse(BaseModel):
    platform: PlatformInfo
    error: Optional[str] = None


class PlatformsResponse(BaseModel):
    platforms: List[PlatformInfo]
    error: Optional[str] = None


class PlatformListRequest(BaseModel):
    cursor: PlatformCursor
    orderBy: str = OrderBy.ASC
    pageSize: int

    class Config:
        use_enum_values = True


class PlatformListResponse(BaseModel):
    platform: List[PlatformInfo] = []
    error: Optional[str] = None


class PlatformRequest(BaseModel):
    appName: str
    externalPlatformId: str
    platformType: str
    url: str
    comment: Optional[str] = None


class BatchPlatformRequest(BaseModel):
    platforms: List[PlatformRequest]


# Контрагенты


class LegalType(str, Enum):
    LEGAL_TYPE_INVALID = "LEGAL_TYPE_INVALID"
    LEGAL_TYPE_LEGAL = "LEGAL_TYPE_LEGAL"
    LEGAL_TYPE_INDIVIDUAL = "LEGAL_TYPE_INDIVIDUAL"
    LEGAL_TYPE_ENTREPRENEUR = "LEGAL_TYPE_ENTREPRENEUR"
    LEGAL_TYPE_FOREIGN_LEGAL = "LEGAL_TYPE_FOREIGN_LEGAL"
    LEGAL_TYPE_FOREIGN_INDIVIDUAL = "LEGAL_TYPE_FOREIGN_INDIVIDUAL"
    LEGAL_TYPE_FOREIGN_ENTREPRENEUR = "LEGAL_TYPE_FOREIGN_ENTREPRENEUR"


class Address(BaseModel):
    address: str
    locality: str
    postcode: str


class OrganisationPlatformInfo(BaseModel):
    appName: str
    externalPlatformId: str
    isPlatformOwner: bool
    platformId: str
    platformType: str
    url: str


class OrganisationData(BaseModel):
    externalOrganisationId: str
    fio: Optional[str] = None
    fullOpf: str
    individualAccountDescription: Optional[str] = None
    inn: str
    isOpc: bool
    isPp: bool
    legalAddress: Address
    legalType: LegalType = LegalType.LEGAL_TYPE_INVALID
    ogrn: Optional[str] = None
    ogrnip: Optional[str] = None
    paymentNumber: Optional[str] = None
    phoneNumber: Optional[str] = None
    platforms: List[OrganisationPlatformInfo] = []
    postAddress: Address
    regionNumber: Optional[str] = None
    registrationNumber: Optional[str] = None
    rsUrl: Optional[str] = None
    shortOpf: Optional[str] = None
    taxId: Optional[str] = None
    trustedPerson: Optional[str] = None
    violationDescription: Optional[str] = None
    updatedAt: Optional[datetime] = None
    comment: Optional[str] = None

    class Config:
        use_enum_values = True


class OrganisationResponse(BaseModel):
    organisation: OrganisationData
    error: Optional[str] = None


class ExternalOrganisationPlatform(BaseModel):
    externalPlatformId: str
    isPlatformOwner: bool


class AddOrganisationPlatformRequest(BaseModel):
    platform: list[ExternalOrganisationPlatform]


class ExternalCursorOrg(BaseModel):
    externalId: Optional[str] = None
    updatedAt: Optional[UpdatedAt] = None


class OrganisationListRequest(BaseModel):
    cursor: Optional[ExternalCursorOrg] = None
    externalOrganisationIds: Optional[List[str]] = []
    gtExternalOrganisationId: Optional[str] = None
    orderBy: str = OrderBy.ASC
    pageSize: int = 2500

    class Config:
        use_enum_values = True


class ExternalExtAuditLogAccount(BaseModel):
    email: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None


class ExtOrganisationExtOrganisationPlatformInfo(BaseModel):
    appName: Optional[str] = None
    createdAt: Optional[str] = None
    createdBy: Optional[ExternalExtAuditLogAccount] = None
    editedAt: Optional[str] = None
    editedBy: Optional[ExternalExtAuditLogAccount] = None
    externalPlatformId: Optional[str] = None
    isPlatformOwner: Optional[bool] = None
    organisationId: Optional[str] = None
    platformType: Optional[str] = None
    url: Optional[str] = None


class ExternalExtOrganisation(BaseModel):
    createdAt: Optional[str] = None
    createdBy: Optional[ExternalExtAuditLogAccount] = None
    editedAt: Optional[str] = None
    editedBy: Optional[ExternalExtAuditLogAccount] = None
    externalOrganisationId: Optional[str] = None
    fio: Optional[str] = None
    fullOpf: Optional[str] = None
    individualAccountDescription: Optional[str] = None
    inn: Optional[str] = None
    isOpc: Optional[bool] = None
    isPp: Optional[bool] = None
    legalAddress: Optional[Address] = None
    legalType: Optional[str] = None
    ogrn: Optional[str] = None
    ogrnip: Optional[str] = None
    organisationPlatformInfo: List[ExtOrganisationExtOrganisationPlatformInfo] = []
    organisationId: Optional[str] = None
    paymentNumber: Optional[str] = None
    phoneNumber: Optional[str] = None
    platforms: List[ExtOrganisationExtOrganisationPlatformInfo] = []
    postAddress: Optional[Address] = None
    regionNumber: Optional[str] = None
    registrationNumber: Optional[str] = None
    rsUrl: Optional[str] = None
    shortOpf: Optional[str] = None
    taxId: Optional[str] = None
    trustedPerson: Optional[str] = None
    violationDescription: Optional[str] = None
    updatedAt: Optional[str] = None
    comment: Optional[str] = None


class OrganisationListResponse(BaseModel):
    organisation: List[ExternalExtOrganisation] = []
    error: Optional[str] = None


# Контракты
class ExternalActionType(str, Enum):
    ACTION_TYPE_INVALID = "ACTION_TYPE_INVALID"
    ACTION_TYPE_CONCLUSION = "ACTION_TYPE_CONCLUSION"
    ACTION_TYPE_DISTRIBUTION = "ACTION_TYPE_DISTRIBUTION"
    ACTION_TYPE_COMMERCIAL = "ACTION_TYPE_COMMERCIAL"
    ACTION_TYPE_OTHER = "ACTION_TYPE_OTHER"


class ExternalContractType(str, Enum):
    CONTRACT_TYPE_INVALID = "CONTRACT_TYPE_INVALID"
    CONTRACT_TYPE_SERVICE = "CONTRACT_TYPE_SERVICE"
    CONTRACT_TYPE_INTERMEDIARY = "CONTRACT_TYPE_INTERMEDIARY"
    CONTRACT_TYPE_ADDITIONAL_AGREEMENT = "CONTRACT_TYPE_ADDITIONAL_AGREEMENT"


class ExternalSubjectType(str, Enum):
    SUBJECT_TYPE_INVALID = "SUBJECT_TYPE_INVALID"
    SUBJECT_TYPE_DISTRIBUTION = "SUBJECT_TYPE_DISTRIBUTION"
    SUBJECT_TYPE_ORGANISATION = "SUBJECT_TYPE_ORGANISATION"
    SUBJECT_TYPE_INTERMEDIARY = "SUBJECT_TYPE_INTERMEDIARY"
    SUBJECT_TYPE_REPRESENTATION = "SUBJECT_TYPE_REPRESENTATION"
    SUBJECT_TYPE_OTHER = "SUBJECT_TYPE_OTHER"


class ContractData(BaseModel):
    actionType: ExternalActionType
    contractDate: str
    contractType: ExternalContractType
    externalContractId: str
    externalOrganisationCustomerId: str
    externalOrganisationPerformerId: str
    subjectType: ExternalSubjectType
    withNds: bool
    additionalContractNumber: Optional[str] = None
    additionalContractNumberDate: Optional[str] = None
    agentActingForPublisher: Optional[bool] = None
    contractNumber: Optional[str] = None
    externalParentId: Optional[str] = None
    isCreativeReporter: Optional[bool] = None
    price: Optional[str] = None
    comment: Optional[str] = None

    class Config:
        use_enum_values = True


class ContractCreator(BaseModel):
    email: Optional[str]
    id: Optional[str]
    name: Optional[str]


class ContractDetails(BaseModel):
    actionType: str
    additionalContractNumber: Optional[str]
    additionalContractNumberDate: Optional[str]
    agentActingForPublisher: bool
    contractDate: str
    contractId: str
    contractNumber: str
    contractType: str
    createdAt: str
    createdBy: Optional[ContractCreator]
    editedAt: Optional[str]
    editedBy: Optional[ContractCreator]
    externalContractId: str
    externalOrganisationCustomerId: str
    externalOrganisationPerformerId: str
    externalParentId: Optional[str]
    isCreativeReporter: bool
    price: str
    subjectType: str
    updatedAt: str
    withNds: bool
    comment: str


class ContractResponse(BaseModel):
    contract: ContractDetails
    error: Optional[str] = None


class ExternalCursorContract(BaseModel):
    externalId: Optional[str]
    updatedAt: Optional[UpdatedAt] = None


class ContractsListResponse(BaseModel):
    contract: List[ContractDetails] = []
    error: Optional[str] = None


class ContractsListRequest(BaseModel):
    cursor: Optional[ExternalCursorContract]
    externalContractIds: Optional[List[str]]
    gtExternalContractId: Optional[str]
    orderBy: str = OrderBy.ASC
    pageSize: int

    class Config:
        use_enum_values = True


# Креативы
class ExternalMediaFileRequest(BaseModel):
    id: str
    originalUrl: Optional[str] = None
    url: Optional[str] = None


class ExternalGeoTarget(BaseModel):
    guid: str
    name: str


class CreativeCreator(BaseModel):
    email: str
    id: str
    name: str


class CreativeEditor(BaseModel):
    email: str
    id: str
    name: str


class ExternalMediaData(BaseModel):
    description: Optional[str] = None
    file: Optional[ExternalMediaFileRequest] = None
    text: Optional[str] = None


class UrlListData(BaseModel):
    url: Optional[str]


class CreativeData(BaseModel):
    advObjectType: str = None
    description: str
    externalContractIds: List[str] = None
    externalContractId: Optional[str] = None
    externalCreativeId: Optional[str] = None
    geoTargets: Optional[List[ExternalGeoTarget]] = None
    isSocialAdv: bool
    isNative: bool
    mediaData: List[ExternalMediaData]
    okvedCodes: List[str]
    paymentType: str
    selfPromotionExternalOrganizationId: Optional[str] = None
    targetLink: Optional[str] = None
    urlList: Optional[List[UrlListData]] = []
    title: str
    comment: Optional[str] = Field(None, max_length=2000)


class CreativeDetailsResponse(BaseModel):
    advObjectType: str
    createdAt: str = None
    createdBy: Optional[CreativeCreator] = None
    creativeId: str = None
    editedAt: Optional[str] = None
    editedBy: Optional[CreativeEditor] = None
    description: str
    externalContractId: str = None
    externalCreativeId: str = None
    geoTargets: List[ExternalGeoTarget]
    isSocialAdv: bool
    marker: str = None
    mediaData: List[ExternalMediaData]
    okvedCodes: List[str]
    paymentType: str
    targetLink: Optional[str] = None
    title: str
    updatedAt: Optional[str] = None
    urlList: Optional[List[UrlListData]] = []
    comment: Optional[str] = Field(None, max_length=2000)


class CreativeResponse(BaseModel):
    creative: Optional[CreativeDetailsResponse] = None
    comment: Optional[str] = None
    error: Optional[str] = None


class ExternalCursorCreative(BaseModel):
    externalId: Optional[str]
    updatedAt: Optional[dict]


class CreativesListResponse(BaseModel):
    creative: List[CreativeDetailsResponse]


class CreativesListRequest(BaseModel):
    cursor: ExternalCursorCreative
    orderBy: str
    pageSize: int


# Загрузка файлов


class FileUploadData(BaseModel):
    file_url: HttpUrl
    bucket: str

    @field_validator("file_url")
    def validate_file_url_extension(cls, value):
        valid_extensions = [
            ".mp4",
            ".jpeg",
            ".jpg",
            ".png",
            ".webp",
            ".zip",
            ".pdf",
            ".html",
            ".css",
        ]
        if not any(value.path.endswith(ext) for ext in valid_extensions):
            raise ValueError(
                f"Unsupported file URL extension: {value.path}. Allowed extensions are {valid_extensions}"
            )
        return value


class FileUploadResponse(BaseModel):
    id: int


class FileDownloadResponse(BaseModel):
    content: bytes = Field(default=None)
    filename: str = None
    error: str = None


class FileUrl:
    url: HttpUrl


# Статистика
class ExternalExtStatistic(BaseModel):
    creativeId: Optional[str] = None
    dateEndFact: str
    dateEndPlan: str
    dateStartFact: str
    dateStartPlan: str
    externalCreativeId: str
    externalPlatformId: str
    externalStatisticId: str
    moneySpent: str
    platformId: Optional[str] = None
    statisticId: Optional[str] = None
    unitCost: str
    viewsCountByFact: str
    viewsCountByInvoice: str
    withNds: bool
    comment: Optional[str] = None


class StatisticList(BaseModel):
    statistics: List[ExternalExtStatistic]


class ExternalExtUpsertStatisticResponse(BaseModel):
    message: Optional[str] = True


class ExternalCursorStatistic(BaseModel):
    externalId: Optional[str] = None
    updatedAt: Optional[UpdatedAt] = None


class StatisticListRequest(BaseModel):
    cursor: Optional[ExternalCursorStatistic] = None
    externalContractIds: Optional[List[str]] = None
    externalCreativeIds: Optional[List[str]] = None
    externalInvoiceIds: Optional[List[str]] = None
    externalPlatformsIds: Optional[List[str]] = None
    gtExternalStatisticId: Optional[str] = None
    invoiceFromDate: Optional[str] = None
    invoiceToDate: Optional[str] = None
    orderBy: Optional[str] = None
    pageSize: Optional[int] = None
    statFromDate: Optional[str] = None
    statPeriodFromDate: Optional[str] = None
    statPeriodToDate: Optional[str] = None
    statToDate: Optional[str] = None
    withoutInvoices: Optional[bool] = None


class StatisticItem(BaseModel):
    contractId: str
    createdAt: Optional[str] = None
    createdBy: Optional[dict]
    creativeName: str
    creativeType: str
    editedAt: Optional[str] = None
    editedBy: Optional[dict]
    externalContractId: str
    externalInvoiceId: str
    invoiceId: str
    platformName: str
    platformType: str
    statistic: dict
    updatedAt: Optional[str] = None
    comment: Optional[str] = None


class StatisticListResponse(BaseModel):
    items: List[StatisticItem]


class StatisticResponse(BaseModel):
    creativeName: str
    creativeType: str
    platformName: str
    platformType: str
    statistic: ExternalExtStatistic
    comment: Optional[str] = None
    error: Optional[str] = None


# Акты
class ExternalContract(BaseModel):
    externalContractId: Optional[str] = None
    price: str
    withNds: bool
    contractId: Optional[str] = None


class User(BaseModel):
    email: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None


class InvoiceCursor(BaseModel):
    externalId: Optional[str]
    updatedAt: Optional[dict] = None


class InvoiceFilter(BaseModel):
    cursor: Optional[InvoiceCursor] = None
    orderBy: Optional[str] = "ASC"
    pageSize: Optional[int] = 20


class InvoiceRequestData(BaseModel):
    clientRole: str
    contractorRole: str
    contracts: List[ExternalContract]
    endDate: str
    externalContractId: str
    externalInvoiceId: str
    invoiceDate: str
    invoiceNumber: str
    price: str
    startDate: str
    violation: Optional[List[str]] = None
    withNds: bool
    comment: Optional[str] = None


class InvoiceResponseData(BaseModel):
    clientRole: str
    contractId: Optional[str] = None
    contractorRole: str
    contracts: List[ExternalContract]
    createdAt: Optional[str] = None
    createdBy: Optional[User] = None
    editedAt: Optional[str] = None
    editedBy: Optional[User] = None
    endDate: str
    externalContractId: str
    externalInvoiceId: str
    invoiceDate: str
    invoiceId: Optional[str] = None
    invoiceNumber: str
    price: str
    startDate: str
    violation: Optional[List[str]] = None
    withNds: bool
    updatedAt: Optional[str] = None
    comment: Optional[str] = None


class InvoiceResponse(BaseModel):
    invoice: InvoiceResponseData


class InvoiceListResponse(BaseModel):
    invoice: List[InvoiceResponseData]
    error: Optional[str] = None


class CreativeLinkItem(BaseModel):
    externalContractId: str
    externalCreativeIds: List[str]
    externalInvoiceId: str


class CreativeLinkRequest(BaseModel):
    items: List[CreativeLinkItem]


class CreativeUnlinkItem(BaseModel):
    deleteAllCreatives: bool
    externalContractId: str
    externalCreativeIds: Optional[List[str]] = None
    externalInvoiceId: str


class CreativeUnlinkRequest(BaseModel):
    items: List[CreativeUnlinkItem]


class CreativeInvoiceLinkQuery(BaseModel):
    externalInvoiceIds: Optional[List[str]] = None
    externalContractIds: Optional[List[str]] = None
    pageSize: Optional[int] = None
    cursor: Optional[str] = None


class CreativeInvoiceLinkItem(BaseModel):
    contractId: str
    creativeId: str
    externalContractId: str
    externalCreativeId: str
    externalInvoiceId: str
    id: str
    invoiceId: str


class CreativeInvoiceLinksResponse(BaseModel):
    items: List[CreativeInvoiceLinkItem]


# Справочники
class BankDictionaryRequest(BaseModel):
    search: Optional[str] = None
    pageSize: Optional[int] = None
    gtBik: Optional[str] = None

    def query_data(self):
        """Возвращает словарь атрибутов с исключением None значений."""
        return {k: v for k, v in self.model_dump().items() if v is not None}


class BankInfo(BaseModel):
    address: str
    bik: str
    correspondent_account: Optional[str] = None
    country: str
    name: str


class CountryDictionaryRequest(BaseModel):
    search: Optional[str] = None

    def query_data(self):
        """Возвращает словарь атрибутов с исключением None значений."""
        return {k: v for k, v in self.model_dump().items() if v is not None}


class CountryInfo(BaseModel):
    country: str
    oksmNumber: str
    shortName: str


class FiasDictionaryRequest(BaseModel):
    search: Optional[str] = None
    pageSize: Optional[int] = None
    gtBik: Optional[str] = None

    def query_data(self):
        """Возвращает словарь атрибутов с исключением None значений."""
        return {k: v for k, v in self.model_dump().items() if v is not None}


class FiasInfo(BaseModel):
    guid: str
    id: str
    level: str
    name: str
    parentId: str
    path: str
    type: str


class OkvedDictionaryRequest(BaseModel):
    search: Optional[str] = None

    def query_data(self):
        """Возвращает словарь атрибутов с исключением None значений."""
        return {k: v for k, v in self.model_dump().items() if v is not None}


class OkvedInfo(BaseModel):
    code: str
    name: str


# Удаление
class DeleteOperationObjectType(str, Enum):
    INVALID = "DELETE_OPERATION_OBJECT_TYPE_INVALID"
    ORGANISATION = "DELETE_OPERATION_OBJECT_TYPE_ORGANISATION"
    CONTRACT = "DELETE_OPERATION_OBJECT_TYPE_CONTRACT"
    CREATIVE = "DELETE_OPERATION_OBJECT_TYPE_CREATIVE"
    PLATFORM = "DELETE_OPERATION_OBJECT_TYPE_PLATFORM"
    STATISTIC = "DELETE_OPERATION_OBJECT_TYPE_STATISTIC"
    INVOICE = "DELETE_OPERATION_OBJECT_TYPE_INVOICE"


class DeleteItemRequest(BaseModel):
    externalObjectId: str
    objectType: DeleteOperationObjectType = DeleteOperationObjectType.INVALID

    class Config:
        use_enum_values = True


class DeleteOperationRequest(BaseModel):
    item: DeleteItemRequest


class DeleteOperationResponse(BaseModel):
    message: Optional[str] = True


class DeleteEntityCountResponseEntityCount(BaseModel):
    count: int
    objectType: DeleteOperationObjectType = DeleteOperationObjectType.INVALID


class DeleteEntityCountResponse(BaseModel):
    entityCount: List[DeleteEntityCountResponseEntityCount]


class RelatedItem(BaseModel):
    externalId: str
    objectId: int
    objectType: DeleteOperationObjectType


class ListRelatedResponse(BaseModel):
    items: List[RelatedItem]


# Нотификация
class ErrorNotificationObjectType(str, Enum):
    INVALID = "ERROR_NOTIFICATION_OBJECT_TYPE_INVALID"
    ORGANISATION = "ERROR_NOTIFICATION_OBJECT_TYPE_ORGANISATION"
    CONTRACT = "ERROR_NOTIFICATION_OBJECT_TYPE_CONTRACT"
    CREATIVE = "ERROR_NOTIFICATION_OBJECT_TYPE_CREATIVE"
    INVOICE = "ERROR_NOTIFICATION_OBJECT_TYPE_INVOICE"
    PLATFORM = "ERROR_NOTIFICATION_OBJECT_TYPE_PLATFORM"


class ErrorNotification(BaseModel):
    date: str
    id: str
    objectId: str
    externalId: str
    objectType: ErrorNotificationObjectType
    text: str
    updatedAt: str
    url: str


class ErrorListResponse(BaseModel):
    notification: List[ErrorNotification]


class NotificationQueryParams(BaseModel):
    pageSize: int = Field(default=10, ge=1)
    gtNotificationId: Optional[str] = None
