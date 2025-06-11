from typing import List, Optional
from pydantic import BaseModel, Field


class TableInfo(BaseModel):
    """Model for table information"""
    name: str = Field(description="Table name")
    schema: str = Field(description="Schema name")
    type: Optional[str] = Field(description="Table type (table, view, etc.)", default=None)


class TablesResponse(BaseModel):
    """Response model for listing tables"""
    sql: str = Field(description="Query used to retrieve the information")
    tables: List[TableInfo] = Field(description="List of tables in the schema")
    schema: str = Field(description="Schema name")
    total_count: int = Field(description="Total number of tables")


class SchemaInfo(BaseModel):
    """Model for schema information"""
    sql:str = Field(description="Query used to retrieve the information")
    name: str = Field(description="Schema name")
    description: Optional[str] = Field(description="Schema description", default=None)


class SchemasResponse(BaseModel):
    """Response model for listing schemas"""
    sql:str = Field(description="Query used to retrieve the information")
    schemas: List[SchemaInfo] = Field(description="List of schemas in the database")
    total_count: int = Field(description="Total number of schemas")


class QueryResult(BaseModel):
    """Model for SQL query results"""
    sql:str = Field(description="Query used to retrieve the information")
    success: bool = Field(description="Whether the query executed successfully")
    data: Optional[List[dict]] = Field(description="Query result data", default=None)
    row_count: Optional[int] = Field(description="Number of rows returned", default=None)
    error_message: Optional[str] = Field(description="Error message if query failed", default=None)
    execution_time_ms: Optional[float] = Field(description="Query execution time in milliseconds", default=None)


class GeneralQueryResponse(BaseModel):
    """Model for general database queries"""
    sql:str = Field(description="Query used to retrieve the information")
    answer: str = Field(description="Answer to the database question")
    sql_used: Optional[str] = Field(description="SQL query used to get the answer", default=None)
    confidence: float = Field(description="Confidence level in the answer (0-1)", default=1.0)
