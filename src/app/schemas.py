from typing import List, Dict
import uuid
from datetime import datetime
from pydantic import Schema, BaseModel


# -----------------------------------------------------------------------------
# APPLICATION MODEL
# -----------------------------------------------------------------------------
class Application(BaseModel):

    application_id: uuid.UUID = Schema(None, title="Unique identifier for a given application")
    name: str = Schema(None, title="Application name", max_length=40)
    description: str = Schema(None, title="Application description", max_length=256)
    callback_url: str = Schema(None, title="Callback URL where access token"
                                           " is returned after authorization", max_length=4000)
    public_key: str = Schema(None, title="Public Cryptographic Key used to validate JWT Signatures", max_length=4096)
    private_key: str = Schema(None, title="Private Cryptographic Key used to validate JWT Signatures", max_length=4096)
    environment: str = Schema(
        None, title="Tag that describes the application's environment (Ex: Dev, Test, Prod)", max_length=50
    )
    configuration: dict = Schema(None, title="Additional configurations for the application")
    last_modified: datetime = Schema(
        None, title="Time stamp of the last modification made to the application definition"
    )
    is_enabled: bool = Schema(
        None, title='If the application is enabled of not to authorize users'
    )
    is_soft_deleted: bool = Schema(None, title="If Application is soft deleted")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# CLAIM PROVIDER MODEL
# -----------------------------------------------------------------------------
class ClaimsProviders(BaseModel):

    provider_id: uuid.UUID = Schema(None, title="Unique identifier to a provider id")
    name: str = Schema(None, title="Claim Provider name", max_length=40)
    description: str = Schema(None, title="Claim Provider description", max_length=256)
    is_local: bool = Schema(None, title="If Claim Provider is local or not")
    config: dict = Schema(None, title="Additional configuration for the Claim Provider")
    implementation_class: str = Schema(None, title="Implementation Class", max_length=200)
    credentials: dict = Schema(None, title="Credentials for the Claim Provider")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# IDENTITY TYPE MODEL
# -----------------------------------------------------------------------------
class IdentityType(BaseModel):

    type_name: str = Schema(None, title="Name for an Identity Type", max_length=40)
    description: str = Schema(None, title="Description for an Identity Type", max_length=256)

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# APPLICATION PROVIDER MODEL
# -----------------------------------------------------------------------------
class ApplicationProvider(BaseModel):

    provider_id: uuid.UUID = Schema(None, title="Unique identifier to a provider id")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for a given application")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# CLAIM MODEL
# -----------------------------------------------------------------------------
class Claim(BaseModel):

    claim_id: uuid.UUID = Schema(None, title="Unique identifier for a claim")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for an application id")
    value: str = Schema(None, title="Value for a claim", max_length=512)
    description: str = Schema(None, title="Claim Description", max_length=256)

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# GROUP MODEL
# -----------------------------------------------------------------------------
class Group(BaseModel):

    group_id: uuid.UUID = Schema(None, title="Unique identifier for a group id")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for an application id")
    name: str = Schema(None, title="Group name", max_length=40)
    description: str = Schema(None, title="Group description", max_length=256)
    properties: dict = Schema(None, title="Additional properties for a group")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# IDENTITY MODEL
# -----------------------------------------------------------------------------
class Identity(BaseModel):

    identity_id: uuid.UUID = Schema(None, title="Unique identifier for an Identity")
    business_id: str = Schema(None, title="Business Id", max_length=40)
    identity_data: dict = Schema(None, title="Additional information for an Identity")
    created: datetime = Schema(None, title="Timestamp when the Identity was created")
    last_modified: datetime = Schema(None, title="Timestamp for the last time made to the Identity definition")
    disabled: bool = Schema(None, title="If Identity is enabled or not")
    type: str = Schema(None, title="", max_length=40)
    is_soft_deleted: bool = Schema(None, title="If Identity is soft deleted")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# APPLICATION IDENTITY MODEL
# -----------------------------------------------------------------------------
class ApplicationIdentity(BaseModel):

    identity_id: uuid.UUID = Schema(None, title="Unique identifier for an Identity")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for an Application")
    created: datetime = Schema(None, title="Timestamp when the Application Identity was created")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# APPLICATION OWNERSHIP MODEL
# -----------------------------------------------------------------------------
class ApplicationOwnership(BaseModel):

    identity_id: uuid.UUID = Schema(None, title="Unique identifier for an Identity")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for an Application")
    created: datetime = Schema(None, title="Timestamp when the Application Ownership was created")
    from_date: datetime = Schema(None, title="Timestamp for when Application Ownership validity starts")
    until_date: datetime = Schema(None, title="Timestamp for when Application Ownership validity ends")
    is_owner: bool = Schema(None, title="If the user is owner")
    is_manager: bool = Schema(None, title="If the user is manager")
    configuration: dict = Schema(None, title="Additional configuration for Application Ownership")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# GROUP CLAIM MODEL
# -----------------------------------------------------------------------------
class GroupClaim(BaseModel):

    group_id: uuid.UUID = Schema(None, title="Unique identifier for Group")
    claim_id: uuid.UUID = Schema(None, title="Unique identifier for a claim")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for a claim")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# IDENTITY CLAIM MODEL
# -----------------------------------------------------------------------------
class IdentityClaim(BaseModel):

    claim_id: uuid.UUID = Schema(None, title="Unique identifier for a claim")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for an application")
    identity_id: uuid.UUID = Schema(None, title="Unique identifier for an identity")
    from_date: datetime = Schema(None, title="Timestamp for when Identity Claim validity starts")
    until_date: datetime = Schema(None, title="Timestamp for when Identity Claim validity ends")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# IDENTITY GROUP MODEL
# -----------------------------------------------------------------------------
class IdentityGroup(BaseModel):

    group_id: uuid.UUID = Schema(None, title="Unique identifier for Group")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for an applications")
    identity_id: uuid.UUID = Schema(None, title="Unique identifier for an identity")

    class Config:
        orm_mode = True


# -----------------------------------------------------------------------------
# PROFILE MODEL
# -----------------------------------------------------------------------------
class Profile(BaseModel):

    identity_id: uuid.UUID = Schema(None, title="Unique identifier for an identity")
    application_id: uuid.UUID = Schema(None, title="Unique identifier for an application")
    profile_data: dict = Schema(None, title="Additional information for a profile")

    class Config:
        orm_mode = True
