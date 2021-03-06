#ifndef NRF_ERROR_H__
#define NRF_ERROR_H__ 
#ifdef __cplusplus
extern "C" {
#endif
#define NRF_ERROR_BASE_NUM (0x0)
#define NRF_ERROR_SDM_BASE_NUM (0x1000)
#define NRF_ERROR_SOC_BASE_NUM (0x2000)
#define NRF_ERROR_STK_BASE_NUM (0x3000)
#define NRF_SUCCESS (NRF_ERROR_BASE_NUM + 0)
#define NRF_ERROR_SVC_HANDLER_MISSING (NRF_ERROR_BASE_NUM + 1)
#define NRF_ERROR_SOFTDEVICE_NOT_ENABLED (NRF_ERROR_BASE_NUM + 2)
#define NRF_ERROR_INTERNAL (NRF_ERROR_BASE_NUM + 3)
#define NRF_ERROR_NO_MEM (NRF_ERROR_BASE_NUM + 4)
#define NRF_ERROR_NOT_FOUND (NRF_ERROR_BASE_NUM + 5)
#define NRF_ERROR_NOT_SUPPORTED (NRF_ERROR_BASE_NUM + 6)
#define NRF_ERROR_INVALID_PARAM (NRF_ERROR_BASE_NUM + 7)
#define NRF_ERROR_INVALID_STATE (NRF_ERROR_BASE_NUM + 8)
#define NRF_ERROR_INVALID_LENGTH (NRF_ERROR_BASE_NUM + 9)
#define NRF_ERROR_INVALID_FLAGS (NRF_ERROR_BASE_NUM + 10)
#define NRF_ERROR_INVALID_DATA (NRF_ERROR_BASE_NUM + 11)
#define NRF_ERROR_DATA_SIZE (NRF_ERROR_BASE_NUM + 12)
#define NRF_ERROR_TIMEOUT (NRF_ERROR_BASE_NUM + 13)
#define NRF_ERROR_NULL (NRF_ERROR_BASE_NUM + 14)
#define NRF_ERROR_FORBIDDEN (NRF_ERROR_BASE_NUM + 15)
#define NRF_ERROR_INVALID_ADDR (NRF_ERROR_BASE_NUM + 16)
#define NRF_ERROR_BUSY (NRF_ERROR_BASE_NUM + 17)
#define NRF_ERROR_CONN_COUNT (NRF_ERROR_BASE_NUM + 18)
#define NRF_ERROR_RESOURCES (NRF_ERROR_BASE_NUM + 19)
#ifdef __cplusplus
}
#endif
#endif
