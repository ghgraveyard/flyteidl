// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: flyteidl/plugins/qubole.proto

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

// Validate checks the field values on HiveQuery with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *HiveQuery) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Query

	// no validation rules for TimeoutSec

	// no validation rules for RetryCount

	return nil
}

// HiveQueryValidationError is the validation error returned by
// HiveQuery.Validate if the designated constraints aren't met.
type HiveQueryValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e HiveQueryValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e HiveQueryValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e HiveQueryValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e HiveQueryValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e HiveQueryValidationError) ErrorName() string { return "HiveQueryValidationError" }

// Error satisfies the builtin error interface
func (e HiveQueryValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sHiveQuery.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = HiveQueryValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = HiveQueryValidationError{}

// Validate checks the field values on HiveQueryCollection with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *HiveQueryCollection) Validate() error {
	if m == nil {
		return nil
	}

	for idx, item := range m.GetQueries() {
		_, _ = idx, item

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return HiveQueryCollectionValidationError{
					field:  fmt.Sprintf("Queries[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	return nil
}

// HiveQueryCollectionValidationError is the validation error returned by
// HiveQueryCollection.Validate if the designated constraints aren't met.
type HiveQueryCollectionValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e HiveQueryCollectionValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e HiveQueryCollectionValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e HiveQueryCollectionValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e HiveQueryCollectionValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e HiveQueryCollectionValidationError) ErrorName() string {
	return "HiveQueryCollectionValidationError"
}

// Error satisfies the builtin error interface
func (e HiveQueryCollectionValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sHiveQueryCollection.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = HiveQueryCollectionValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = HiveQueryCollectionValidationError{}

// Validate checks the field values on QuboleHiveJob with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *QuboleHiveJob) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for ClusterLabel

	if v, ok := interface{}(m.GetQueryCollection()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return QuboleHiveJobValidationError{
				field:  "QueryCollection",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// QuboleHiveJobValidationError is the validation error returned by
// QuboleHiveJob.Validate if the designated constraints aren't met.
type QuboleHiveJobValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e QuboleHiveJobValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e QuboleHiveJobValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e QuboleHiveJobValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e QuboleHiveJobValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e QuboleHiveJobValidationError) ErrorName() string { return "QuboleHiveJobValidationError" }

// Error satisfies the builtin error interface
func (e QuboleHiveJobValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sQuboleHiveJob.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = QuboleHiveJobValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = QuboleHiveJobValidationError{}
