CREATE OR REPLACE PACKAGE "kesplus_platform"."http"  AS
    /**
     * @Description 发送http请求（get）
     * @param URL 地址
     * @Return json
     */
    FUNCTION GET(URL TEXT) RETURN JSON ;
    /**
     * @Description 发送http请求（get）
     * @param URL 地址
     * @param HEADER_JSON 请求头
     * @Return json
     */
    FUNCTION GET(URL TEXT,HEADER_JSON JSON) RETURN JSON;
    /**
     * @Description 发送http请求（post）
     * @param URL 地址
     * @param BODY_CONTENT 请求头
     * @Return json
     */
    FUNCTION POST(URL TEXT,BODY_CONTENT JSON) RETURN JSON;
    /**
     * @Description 发送http请求（post）
     * @param URL 地址
     * @param BODY_CONTENT 请求内容
     * @param HEADER_JSON 请求头
     * @param CONTENT_TYPE 请求内容类型 默认 application/json
     * @Return json
     */
    FUNCTION POST(URL TEXT,BODY_CONTENT JSON,HEADER_JSON JSON,CONTENT_TYPE TEXT DEFAULT 'application/json') RETURN JSON;
    FUNCTION PUT(URL TEXT,BODY_CONTENT JSON) RETURN JSON;
    FUNCTION PUT(URL TEXT,BODY_CONTENT JSON,HEADER_JSON JSON,CONTENT_TYPE TEXT DEFAULT 'application/json') RETURN JSON;
    FUNCTION DELETE(URL TEXT) RETURN JSON;
    FUNCTION BUILD_HEADER_ARRAY(HEADER_JSON JSON) RETURN http_header[];
    FUNCTION REQUEST(METHOD TEXT,URL TEXT,HEADERS http_header[],CONTENT_TYPE TEXT DEFAULT 'application/json',BODY_CONTENT JSON) RETURN JSON;
    FUNCTION CONTENT_CONVERT(REC RECORD) RETURN JSON;
END;

CREATE OR REPLACE PACKAGE BODY "kesplus_platform"."http" AS WRAPPED
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
I/HnejJ4IvYHChEGp8PloA==
END;

