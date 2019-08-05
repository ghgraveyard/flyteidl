/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type CoreWorkflowExecutionPhase string

// List of coreWorkflowExecutionPhase
const (
	CoreWorkflowExecutionPhaseUNDEFINED CoreWorkflowExecutionPhase = "UNDEFINED"
	CoreWorkflowExecutionPhaseQUEUED CoreWorkflowExecutionPhase = "QUEUED"
	CoreWorkflowExecutionPhaseRUNNING CoreWorkflowExecutionPhase = "RUNNING"
	CoreWorkflowExecutionPhaseSUCCEEDING CoreWorkflowExecutionPhase = "SUCCEEDING"
	CoreWorkflowExecutionPhaseSUCCEEDED CoreWorkflowExecutionPhase = "SUCCEEDED"
	CoreWorkflowExecutionPhaseFAILING CoreWorkflowExecutionPhase = "FAILING"
	CoreWorkflowExecutionPhaseFAILED CoreWorkflowExecutionPhase = "FAILED"
	CoreWorkflowExecutionPhaseABORTED CoreWorkflowExecutionPhase = "ABORTED"
	CoreWorkflowExecutionPhaseTIMED_OUT CoreWorkflowExecutionPhase = "TIMED_OUT"
)
