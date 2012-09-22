/*
 * Author: Javi Roman <javiroman@kernel-labs.org>
 */
#include <konkret/konkret.h>
#include <strings.h>
#include "Widget.h"

static const CMPIBroker* _cb = NULL;

static void WidgetInitialize()
{
}

static CMPIStatus WidgetCleanup(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    CMPIBoolean term)
{
    CMReturn(CMPI_RC_OK);
}

static CMPIStatus WidgetEnumInstanceNames(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop)
{
    return KDefaultEnumerateInstanceNames(
        _cb, mi, cc, cr, cop);
}

static CMPIStatus WidgetEnumInstances(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop,
    const char** properties)
{

         Widget w;
     
         /* Widget.Id="1001" */
	Widget_Init(&w, _cb, KNameSpace(cop));
	Widget_Set_Id(&w, "1001");
	Widget_Set_Color(&w, "Red");
	Widget_Set_Size(&w, 1);
	KReturnInstance(cr, w);
     
	/* Widget.Id="1002" */
	Widget_Init(&w, _cb, KNameSpace(cop));
	Widget_Set_Id(&w, "1002");
	Widget_Set_Color(&w, "Green");
	Widget_Set_Size(&w, 2);
	KReturnInstance(cr, w);

	/* Widget.Id="1003" */
	Widget_Init(&w, _cb, KNameSpace(cop));
	Widget_Set_Id(&w, "1003");
	Widget_Set_Color(&w, "Blue");
	Widget_Set_Size(&w, 3); 
    KReturnInstance(cr, w);
 
    CMReturn(CMPI_RC_OK);
}
        
static CMPIStatus WidgetGetInstance(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop,
    const char** properties)
{
    return KDefaultGetInstance(
        _cb, mi, cc, cr, cop, properties);
}

static CMPIStatus WidgetCreateInstance(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop,
    const CMPIInstance* ci)
{
    CMReturn(CMPI_RC_ERR_NOT_SUPPORTED);
}

static CMPIStatus WidgetModifyInstance(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop,
    const CMPIInstance* ci,
    const char** properties)
{
    CMReturn(CMPI_RC_ERR_NOT_SUPPORTED);
}

static CMPIStatus WidgetDeleteInstance(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop)
{
    CMReturn(CMPI_RC_ERR_NOT_SUPPORTED);
}

static CMPIStatus WidgetExecQuery(
    CMPIInstanceMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop,
    const char* lang,
    const char* query)
{
    CMReturn(CMPI_RC_ERR_NOT_SUPPORTED);
}

CMInstanceMIStub(
    Widget,
    KC_Widget,
    _cb,
    WidgetInitialize())

static CMPIStatus WidgetMethodCleanup(
    CMPIMethodMI* mi,
    const CMPIContext* cc,
    CMPIBoolean term)
{
    CMReturn(CMPI_RC_OK);
}

static CMPIStatus WidgetInvokeMethod(
    CMPIMethodMI* mi,
    const CMPIContext* cc,
    const CMPIResult* cr,
    const CMPIObjectPath* cop,
    const char* meth,
    const CMPIArgs* in,
    CMPIArgs* out)
{
    return Widget_DispatchMethod(
        _cb, mi, cc, cr, cop, meth, in, out);
}

CMMethodMIStub(
    Widget,
    KC_Widget,
    _cb,
    WidgetInitialize())

KUint32 Widget_Add(
    const CMPIBroker* cb,
    CMPIMethodMI* mi,
    const CMPIContext* context,
    const WidgetRef* self,
    const KUint32* X,
    const KUint32* Y,
    CMPIStatus* status)
{
    printf("Widget_Add method invoked\n");

    KUint32 result = KUINT32_INIT;

    if (!X->exists || !Y->exists || X->null || Y->null) {
        KSetStatus(status, ERR_INVALID_PARAMETER);
        return result;
    }
     
    KUint32_Set(&result, X->value + Y->value);
    KSetStatus(status, OK);

    printf("result: %d\n", result.value);

    return result;
}

KONKRET_REGISTRATION(
    "root/cimv2",
    "KC_Widget",
    "KC_Widget",
    "instance method")

/* vim: set ts=4 et sw=4 tw=0 sts=4: */
