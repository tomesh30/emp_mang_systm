-- V1__init_audit.sql
CREATE TABLE AuditLog (
    LogId INT IDENTITY(1,1) PRIMARY KEY,
    Action NVARCHAR(100) NOT NULL,
    TriggeredBy NVARCHAR(100) DEFAULT SYSTEM_USER,
    CreatedAt DATETIME2 DEFAULT SYSDATETIME()
);
GO

INSERT INTO AuditLog (Action) VALUES ('CI/CD Deployment Initialized');
GO