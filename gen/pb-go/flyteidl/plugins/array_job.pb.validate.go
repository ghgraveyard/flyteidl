// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: flyteidl/plugins/array_job.proto

package plugins

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/golang/protobuf/ptypes"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = ptypes.DynamicAny{}
)

// Validate checks the field values on ArrayJob with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *ArrayJob) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Parallelism

	// no validation rules for Size

	// no validation rules for MinSuccesses

	return nil
}

// ArrayJobValidationError is the validation error returned by
// ArrayJob.Validate if the designated constraints aren't met.
type ArrayJobValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ArrayJobValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ArrayJobValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ArrayJobValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ArrayJobValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ArrayJobValidationError) ErrorName() string { return "ArrayJobValidationError" }

// Error satisfies the builtin error interface
func (e ArrayJobValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sArrayJob.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ArrayJobValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ArrayJobValidationError{}
